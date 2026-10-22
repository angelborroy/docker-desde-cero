"""Exercise CRUD, non-root execution, persistence, recovery and both databases.

Uses unique container, volume and project names. Never cleans unrelated resources.
Requires Python 3 and access to the Docker daemon. Run from any directory.
"""
from pathlib import Path
import json
import os
import subprocess
import time
import urllib.request
import uuid

COURSE = Path(__file__).resolve().parent.parent
RUN_ID = 'training-test-' + uuid.uuid4().hex[:10]
IMAGE = 'training-tasks:workshop'
CONTAINER = RUN_ID + '-sqlite'
VOLUME = RUN_ID + '-sqlite'
environment = {**os.environ, 'APP_PORT': '0', 'DB_PASSWORD': 'classroom-only'}


def command(*args, check=True):
    result = subprocess.run(['docker', *args], cwd=COURSE, env=environment,
                            text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if check and result.returncode:
        raise RuntimeError(' '.join(args) + '\n' + result.stdout + result.stderr)
    return result.stdout.strip()


def compose(*args, failure=False):
    files = ['-f', 'compose.yaml']
    if failure:
        files += ['-f', 'examples/compose.failure.yaml']
    return command('compose', '-p', RUN_ID, *files, *args)


def js(container, source):
    return command('exec', container, 'node', '-e', source)


def wait(container):
    for _ in range(90):
        try:
            js(container, "fetch('http://localhost:3000/items').then(r=>process.exit(r.ok?0:1)).catch(()=>process.exit(1))")
            return
        except RuntimeError:
            time.sleep(1)
    raise RuntimeError('Application did not become ready: ' + command('logs', container))


def create(container, name):
    return json.loads(js(container, "fetch('http://localhost:3000/items', {method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({name:" + json.dumps(name) + "})}).then(r=>r.json()).then(x=>console.log(JSON.stringify(x)))"))


def items(container):
    return json.loads(js(container, "fetch('http://localhost:3000/items').then(r=>r.json()).then(x=>console.log(JSON.stringify(x)))"))


def start_sqlite(volume=False):
    args = ['run', '-d', '--name', CONTAINER]
    if volume:
        args += ['--mount', f'type=volume,source={VOLUME},target=/data']
    command(*args, IMAGE)
    wait(CONTAINER)


# Student material and reference solutions.
# Each case: (name, dockerfile relative to COURSE or None for the folder default,
# build context, container port, request path, expected substring, non-root).
MATERIAL = [
    ('first-build', None, 'material/first-build', 80, '/', 'Congrats', False),
    ('simple-python-webapp', 'solutions/simple-python-webapp/Dockerfile',
     'material/simple-python-webapp', 5000, '/', 'Hello world!', False),
    ('nonroot-node-app', 'solutions/nonroot-node-app/Dockerfile',
     'material/nonroot-node-app', 3000, '/api/message', 'Hello world!', True),
    ('multi-stage-react-app', 'solutions/multi-stage-react-app/Dockerfile',
     'material/multi-stage-react-app', 80, '/', 'Vite + React', False),
    ('security-lab', 'solutions/security-lab/Dockerfile',
     'material/security-lab', 8080, '/math?factorize=12', '2 2 3', True),
]


def http_body(port, path):
    with urllib.request.urlopen('http://127.0.0.1:' + str(port) + path, timeout=5) as response:
        return response.status, response.read().decode('utf-8', 'replace')


def wait_http(port, path):
    for _ in range(120):
        try:
            status, body = http_body(port, path)
            if status == 200:
                return body
        except Exception:
            pass
        time.sleep(1)
    raise RuntimeError('Endpoint ' + path + ' on port ' + str(port) + ' did not become ready')


def host_port(container, container_port):
    mapping = command('port', container, str(container_port)).splitlines()[0]
    return mapping.rsplit(':', 1)[1]


def test_material():
    images = []
    containers = []
    try:
        for name, dockerfile, context, port, path, expected, nonroot in MATERIAL:
            tag = RUN_ID + '-mat-' + name
            container = tag
            build = ['build', '-t', tag]
            if dockerfile:
                build += ['-f', dockerfile]
            command(*build, context)
            images.append(tag)
            command('run', '-d', '--name', container, '-p', '127.0.0.1::' + str(port), tag)
            containers.append(container)
            body = wait_http(host_port(container, port), path)
            assert expected in body, name + ': unexpected response ' + repr(body[:200])
            if nonroot:
                assert command('exec', container, 'id', '-u') != '0', name + ': runs as root'
        print('PASS: material and solutions build, serve and run non-root where required', flush=True)
    finally:
        if containers:
            command('rm', '-f', *containers, check=False)
        for tag in images:
            command('rmi', '-f', tag, check=False)


if __name__ == '__main__':
    command('info')
    test_material()
    command('build', '-t', IMAGE, './app')
    try:
        start_sqlite()
        item = create(CONTAINER, 'ephemeral')
        command('stop', CONTAINER)
        command('start', CONTAINER)
        wait(CONTAINER)
        assert items(CONTAINER)[0]['id'] == item['id'], 'Stop/start lost data'
        command('rm', '-f', CONTAINER)
        start_sqlite()
        assert items(CONTAINER) == [], 'Recreated container kept ephemeral data'
        command('rm', '-f', CONTAINER)
        command('volume', 'create', VOLUME)
        start_sqlite(volume=True)
        item = create(CONTAINER, 'persistent')
        command('rm', '-f', CONTAINER)
        start_sqlite(volume=True)
        assert items(CONTAINER)[0]['id'] == item['id'], 'Volume lost data'
        assert js(CONTAINER, 'console.log(process.getuid())') != '0', 'App runs as root'
        print('PASS: SQLite, lifecycle, named volume and non-root', flush=True)

        compose('up', '-d', '--wait', '--wait-timeout', '180')
        app = compose('ps', '-q', 'app')
        item = create(app, 'mysql-persistent')
        js(app, "fetch('http://localhost:3000/items/" + item['id'] + "', {method:'PUT',headers:{'Content-Type':'application/json'},body:JSON.stringify({name:'updated',completed:true})}).then(r=>{if(!r.ok)process.exit(1)})")
        assert items(app)[0]['completed'], 'Update failed'
        compose('down')
        compose('up', '-d', '--wait', '--wait-timeout', '180')
        app = compose('ps', '-q', 'app')
        assert items(app)[0]['id'] == item['id'], 'Compose lost data'
        compose('up', '-d', failure=True)
        time.sleep(12)
        failed_app = compose('ps', '-a', '-q', 'app')
        assert command('inspect', '-f', '{{.State.Status}}', failed_app) == 'exited', 'Broken configuration unexpectedly running'
        compose('up', '-d', '--wait', '--wait-timeout', '180')
        app = compose('ps', '-q', 'app')
        assert items(app)[0]['id'] == item['id'], 'Recovery lost data'
        js(app, "fetch('http://localhost:3000/items/" + item['id'] + "',{method:'DELETE'}).then(r=>{if(!r.ok)process.exit(1)})")
        assert items(app) == [], 'Delete failed'
        print('PASS: MySQL CRUD, Compose persistence and failure recovery', flush=True)
    finally:
        command('rm', '-f', CONTAINER, check=False)
        command('volume', 'rm', VOLUME, check=False)
        command('compose', '-p', RUN_ID, '-f', 'compose.yaml', 'down', '-v', '--remove-orphans', check=False)
