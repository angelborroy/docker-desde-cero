# Soluciones de las 23 prácticas

[Prácticas](01-practicas.md) | [Índice](../README.md)

Ejecuta desde la raíz, con Docker iniciado. Revisa primero los nombres y puertos
con `docker ps -a`; las limpiezas se refieren solo a contenedores de estos ejercicios.
En Windows PowerShell usa `curl.exe` para los comandos HTTP.
Estas soluciones son públicas: sirven para comprobar razonamientos y recuperar
el hilo. No hay un manual diferente para el profesor.

## Práctica 1

**Ciclo de vida**

```sh
docker run --name hello-world hello-world
docker run --name timer -it --rm ubuntu:24.04 sleep 30
docker rm hello-world
```
`timer` se elimina al terminar. `hello-world` queda parado hasta eliminarlo.
La imagen es la plantilla; `docker run` crea un contenedor nuevo cada vez.
Dos contenedores no pueden tener el mismo nombre: si `docker run` falla por el
nombre, busca el anterior con `docker ps -a`.

## Práctica 2

**Parámetros de ejecución**

```sh
docker run -d --name nginx -p 127.0.0.1:8080:80 nginx:1.30.6-alpine
docker run -d --name practice-db --label app=mysql -e MYSQL_ROOT_PASSWORD=secret -e MYSQL_DATABASE=app mysql:9.7.2
```
Abre http://localhost:8080. La base no necesita publicar 3306.
`127.0.0.1` restringe la publicación a tu equipo.
Al terminar, elimina los contenedores de esta práctica y sus volúmenes anónimos:

```sh
docker rm -fv nginx practice-db
```

## Práctica 3

**Salud**

```sh
docker run -d --name cats --label app=cats -p 127.0.0.1:5050:5000 --health-cmd "curl -f http://localhost:5000" --health-interval=5s mikesir87/cats:1.0
docker ps
docker inspect --format '{{json .State.Health}}' cats
docker rm -f cats
```
Espera a ver `healthy` antes de eliminarlo. Es una imagen de terceros para la
práctica, no una base recomendada para producción. `unhealthy` no reinicia por sí solo.

## Práctica 4

**Capa escribible**

```sh
docker run -d --name web -p 127.0.0.1:8080:80 nginx:1.30.6-alpine
docker exec web sh -c "echo Hello > /usr/share/nginx/html/hello.html"
docker stop web
docker start web
```
La página http://localhost:8080/hello.html sigue existiendo: `stop` termina el
proceso sin eliminar la capa escribible, y `start` arranca ese mismo contenedor.
Después:

```sh
docker rm -f web
docker run -d --name web -p 127.0.0.1:8080:80 nginx:1.30.6-alpine
```
La página devuelve 404: `rm` eliminó la capa escribible y el fichero no estaba
en un volumen. Limpieza: `docker rm -f web`.

## Práctica 5

**Volúmenes**

```sh
docker volume create volume1
docker volume create database-files
docker run -d --name persistent-db --label app=persistent-db -e MYSQL_ROOT_PASSWORD=root -v database-files:/var/lib/mysql mysql:9.7.2
docker rm -f persistent-db
docker volume ls
```
El volumen nombrado permanece. Eliminar un contenedor o una imagen no elimina
sus volúmenes. Para borrar exclusivamente estos datos de prueba:
`docker volume rm volume1 database-files`.

## Práctica 6

**Inicialización**

```sh
docker run -d --name init-db -v ./material/database-initialization:/docker-entrypoint-initdb.d:ro -e MYSQL_DATABASE=workshop -e MYSQL_ROOT_PASSWORD=secret mysql:9.7.2
docker logs init-db
docker exec init-db mysql -h 127.0.0.1 -uroot -psecret -e "SELECT * FROM workshop.users"
```
Repite la consulta hasta que la inicialización finalice: aparecen Moby Dock y
Whale Watcher. Los scripts no se repiten sobre datos ya inicializados.
Limpieza de este contenedor y su volumen anónimo: `docker rm -fv init-db`.

## Práctica 7

**Desarrollo**

```sh
docker run --name node-app -it --rm -v ./material/dev-express:/app:ro --user node --workdir /app -p 127.0.0.1:3000:3000 node:24.22.0-alpine npm run dev
```
Abre http://localhost:3000/api/message y edita el mensaje en el host. `node --watch`
reinicia el proceso. El montaje es de lectura para el contenedor, pero el editor
del host puede modificarlo. En una imagen ya construida, el mismo cambio no se
ve: el código está copiado dentro de la imagen y hay que reconstruirla.
Ctrl+C termina la práctica.

## Práctica 8

**Persistencia SQLite**

```sh
docker build -t training-tasks:workshop ./app
docker volume create training-sqlite
docker run -d --name training-app -p 127.0.0.1:8080:3000 --mount type=volume,source=training-sqlite,target=/data training-tasks:workshop
```
Crea una tarea en http://localhost:8080. La aplicación escucha en 3000 dentro
del contenedor; el navegador entra por 8080 en tu equipo. `EXPOSE 3000` no
publica el puerto: lo hace `-p`. Después:

```sh
docker rm -f training-app
docker run -d --name training-app -p 127.0.0.1:8080:3000 --mount type=volume,source=training-sqlite,target=/data training-tasks:workshop
```
La tarea permanece porque `/data/todo.db` vive en el volumen. Sin `--mount`, el
nuevo contenedor usa otra base vacía en su capa escribible. El volumen vacío
recibe al principio el contenido y los permisos de `/data` de la imagen,
preparados para el usuario `node`. En Docker Desktop, su ruta física pertenece
al motor Linux, no al sistema de ficheros visible de macOS o Windows.

Un bind mount conecta una carpeta concreta del equipo; es útil para código.
Un volumen lo gestiona Docker; aquí lo usamos para datos. Ninguno sustituye
una copia de seguridad.

Para liberar el puerto para las prácticas siguientes: `docker rm -f training-app`.
Conserva `training-sqlite` hasta el final del curso.

## Práctica 9

**Primera imagen**

```sh
docker build -t first-build material/first-build
docker run --rm -p 127.0.0.1:8080:80 first-build
```
Abre http://localhost:8080 y termina con Ctrl+C. Consulta `docker image history first-build`.
`COPY src` incorpora el sitio; las capas inferiores vienen de `nginx`. Las
instrucciones de metadatos no son capas de ficheros. `material/first-build` es el
contexto: `COPY` solo puede leer ficheros de esa carpeta.

## Práctica 10

**Python**

La referencia es [solutions/simple-python-webapp/Dockerfile](../solutions/simple-python-webapp/Dockerfile).
Para comprobarla sin sobrescribir tu ejercicio:

```sh
docker build -t simple-python-webapp -f solutions/simple-python-webapp/Dockerfile material/simple-python-webapp
docker run --rm -p 127.0.0.1:5000:5000 simple-python-webapp
```
Abre http://localhost:5000 y termina con Ctrl+C. Si el host reserva 5000, publica
`127.0.0.1:5051:5000` y abre 5051. Flask usa su servidor de desarrollo: no es una
plantilla de producción. El ejemplo introduce Dockerfile; el siguiente introduce no root.

## Práctica 11

**Usuario no root**

La referencia es [solutions/nonroot-node-app/Dockerfile](../solutions/nonroot-node-app/Dockerfile).

```sh
docker build -t nonroot-node-app -f solutions/nonroot-node-app/Dockerfile material/nonroot-node-app
docker run -d --name nonroot -p 127.0.0.1:3000:3000 nonroot-node-app
docker exec nonroot id
```
Abre http://localhost:3000/api/message. El UID es 10000. `USER` no cambia el
propietario de ficheros existentes. Por eso `USER` va antes de `WORKDIR`: así
`WORKDIR` crea el directorio con el usuario como propietario. Los ficheros se
copian con `COPY --chown`. Limpieza: `docker rm -f nonroot`.

## Práctica 12

**Multi-stage**

La referencia es [solutions/multi-stage-react-app/Dockerfile](../solutions/multi-stage-react-app/Dockerfile).

```sh
docker build -t multi-stage-react-app -f solutions/multi-stage-react-app/Dockerfile material/multi-stage-react-app
docker run --rm -p 127.0.0.1:8080:80 multi-stage-react-app
docker image ls
```
Abre http://localhost:8080 y termina con Ctrl+C. La etapa final contiene nginx y
los recursos web, sin Node ni dependencias de construcción: por eso es mucho más
pequeña que `node:24.22.0-alpine`. El JavaScript del navegador es público, aunque
esté minificado. La imagen nginx oficial inicia su proceso maestro como root y
reduce privilegios en los workers; no basta con añadir `USER` sin adaptar
permisos y configuración.

## Práctica 13

**Caché**

Recupera primero la aplicación de la práctica 8:

```sh
docker run -d --name training-app -p 127.0.0.1:8080:3000 --mount type=volume,source=training-sqlite,target=/data training-tasks:workshop
```
Cambia el título en `app/src/static/index.html` y construye:

```sh
docker build --progress=plain -t training-tasks:v2 ./app
```
El contenedor existente sigue mostrando la imagen anterior: una imagen nueva no
cambia un contenedor ya creado. `npm ci` aparece como `CACHED` si la base y los
manifiestos no cambiaron: el Dockerfile copia primero los manifiestos y después
el código. Si `COPY src` estuviese antes de `RUN npm ci`, cualquier cambio de
código invalidaría la instalación y todas las instrucciones posteriores.
Ahora recrea el contenedor:

```sh
docker rm -f training-app
docker run -d --name training-app -p 127.0.0.1:8080:3000 --mount type=volume,source=training-sqlite,target=/data training-tasks:v2
```
La tarea sigue ahí: está en el volumen. Restaura el título y prepara la imagen
para las prácticas de redes y Compose:

```sh
docker rm -f training-app
docker build -t training-tasks:workshop ./app
```

## Práctica 14

**DNS**

```sh
docker network create getting-started
docker run -d --name networked-db -e MYSQL_ROOT_PASSWORD=secret -e MYSQL_DATABASE=app --network getting-started --network-alias db mysql:9.7.2
docker run --rm --network getting-started busybox:1.37 nslookup db
docker rm -fv networked-db
docker network rm getting-started
```
El DNS resuelve `db` dentro de la red creada. Resolver un nombre no demuestra
que MySQL ya acepte conexiones.

## Práctica 15

**MySQL para WordPress**

```sh
docker network create wordpress
docker run -d --name wp-db -e MYSQL_ROOT_PASSWORD=secret -e MYSQL_DATABASE=wordpress -e MYSQL_USER=manager -e MYSQL_PASSWORD=secret --network wordpress --network-alias db mysql:9.7.2
docker exec wp-db mysql -h 127.0.0.1 -umanager -psecret -D wordpress -e "SELECT 1"
```
Repite la consulta hasta obtener 1 antes de iniciar WordPress. El usuario `manager`
está limitado a la base `wordpress`; la aplicación no usa root.

## Práctica 16

**WordPress**

```sh
docker run -d --name wp -e WORDPRESS_DB_HOST=db -e WORDPRESS_DB_USER=manager -e WORDPRESS_DB_PASSWORD=secret -e WORDPRESS_DB_NAME=wordpress -p 127.0.0.1:8080:80 --network wordpress wordpress:7.1.3-apache
```
Abre http://localhost:8080 y completa la instalación. Al terminar, borra los datos
anónimos de esta demostración, que no se reutilizan en Compose:

```sh
docker rm -fv wp wp-db
docker network rm wordpress
```

## Práctica 17

**Docker Tasks con MySQL**

```sh
docker network create training-net
docker volume create training-mysql
docker run -d --name training-db --network training-net --network-alias db -e MYSQL_RANDOM_ROOT_PASSWORD=yes -e MYSQL_DATABASE=tasks -e MYSQL_USER=tasks -e MYSQL_PASSWORD=classroom-only --mount type=volume,source=training-mysql,target=/var/lib/mysql mysql:9.7.2
docker exec -e MYSQL_PWD=classroom-only training-db mysql -h 127.0.0.1 -u tasks -D tasks -e "SELECT 1"
```
La primera inicialización puede tardar. Repite la consulta hasta obtener 1. Luego:

```sh
docker run -d --name training-app --network training-net -p 127.0.0.1:8080:3000 -e MYSQL_HOST=db -e MYSQL_USER=tasks -e MYSQL_PASSWORD=classroom-only -e MYSQL_DB=tasks training-tasks:workshop
```
Crea una tarea y consúltala:

```sh
docker exec -e MYSQL_PWD=classroom-only training-db mysql -u tasks -D tasks -e "SELECT name FROM todo_items"
docker rm -f training-app training-db
docker network rm training-net
```
Respuestas a las preguntas:

- `db` se resuelve con el DNS de la red `training-net`. El navegador está fuera de
  esa red, en tu equipo, y no conoce ese nombre.
- La aplicación usa el puerto 3306 dentro de la red. Publicarlo en el equipo
  solo añadiría una vía de acceso innecesaria.
- Con `MYSQL_HOST=localhost`, la aplicación buscaría MySQL dentro de su propio
  contenedor, y allí no hay ninguna base de datos.

El usuario `tasks` accede solo a la base `tasks`; no es root. El volumen
`training-mysql` permanece. `MYSQL_PWD` solo simplifica esta demostración: las
credenciales reales deben usar un fichero protegido o un gestor de secretos.

## Práctica 18

**WordPress con Compose**

La solución completa es [examples/compose.wordpress.yaml](../examples/compose.wordpress.yaml).
Puedes copiarla a `wordpress-compose/compose.yaml` y ejecutar allí Compose.
Para probar la referencia directamente desde la raíz:

```sh
docker compose -f examples/compose.wordpress.yaml up -d --wait
docker compose -f examples/compose.wordpress.yaml ps
```
Abre http://localhost:8080. Respuestas a las preguntas:

- Compose crea una red para el proyecto y cada servicio se resuelve por su
  nombre. `db` es el nombre del servicio, así que no hace falta un alias.
- `docker compose down` elimina contenedores y red, pero conserva los volúmenes
  nombrados. `docker compose down -v` también borra los volúmenes y sus datos.
- WordPress llega a MySQL por la red del proyecto. Nadie fuera de ella necesita
  el puerto 3306.

La referencia mejora los comandos del enunciado: la clave de root es aleatoria
(`MYSQL_RANDOM_ROOT_PASSWORD`) y la clave de `manager` es `classroom-only`, igual
que en Docker Tasks. Las dos variantes funcionan. La consulta SQL del healthcheck
valida la base y el usuario, y `service_healthy` retrasa WordPress hasta entonces.

```sh
docker compose -f examples/compose.wordpress.yaml down
```
Los volúmenes permanecen. Añade `-v` solo para borrar los datos de esta práctica.

## Práctica 19

**Docker Tasks con Compose**

La solución completa es [compose.yaml](../compose.yaml). Si quedan contenedores
manuales de la práctica 17, elimina **solo** `training-app` y `training-db` con
`docker rm -f training-app training-db`.

```sh
docker compose config
docker compose up -d --build --wait
docker compose ps
docker compose exec app id
```
Los servicios `app` y `db` quedan saludables y el proceso de la aplicación no es
root. Crea una tarea, ejecuta `docker compose down` y vuelve a arrancar con
`docker compose up -d --wait`: la tarea permanece. Compose crea una red y un
volumen propios del proyecto `training-docker`; no reutiliza el volumen manual
`training-mysql`. `depends_on` con `service_healthy` espera una consulta SQL válida
al arrancar; no garantiza que la base de datos no falle después.

Extra: copia `.env.example` a `.env` con el editor, cambia `APP_PORT=8081` y
ejecuta `docker compose up -d --wait`. Abre http://localhost:8081 y restaura
8080 al terminar. `APP_PORT` se interpola en `compose.yaml` desde `.env`;
`MYSQL_PASSWORD` se inyecta en los procesos. Son mecanismos distintos. Cambiar
`MYSQL_PASSWORD` no cambia usuarios en un volumen ya inicializado: MySQL solo
los crea en su primera inicialización. `docker compose config` muestra la
configuración resuelta, con las contraseñas: no la publiques con credenciales reales.

## Práctica 20

**Diagnóstico**

```sh
docker compose -f compose.yaml -f examples/compose.failure.yaml up -d
docker compose ps -a
docker compose logs app
docker compose -f compose.yaml -f examples/compose.failure.yaml config
```
Espera a que la aplicación termine antes de observar el estado final. `logs`
muestra el fallo y `config` su causa: el override cambia `MYSQL_HOST` a
`db-inexistente`. Es un error de configuración en ejecución, no del código de la
imagen: por eso reconstruir no lo arregla. Recupera sin borrar datos:

```sh
docker compose -f compose.yaml up -d --wait
docker compose exec app id
docker compose port app 3000
```
Con solo el fichero base vuelve `MYSQL_HOST=db` y Compose recrea el servicio.
Las tareas siguen ahí. `down -v` perdería los datos innecesariamente.

## Práctica 21

**Scout**

```sh
docker build -t demo-service material/scout-demo
docker scout quickview demo-service
docker scout cves --only-severity critical,high demo-service
docker scout recommendations demo-service
```
El ejemplo mantiene Node 18 y Express antiguo intencionadamente. La solución del
enunciado cambia en el `Dockerfile` la línea `ARG NODE_VERSION=18` por
`ARG NODE_VERSION=24`. Para probarlo sin editar el fichero de partida:

```sh
docker build --pull --build-arg NODE_VERSION=24.22.0 -t demo-service:updated material/scout-demo
docker scout cves --only-severity critical,high demo-service:updated
```
Los recuentos no son una salida fija ni se garantiza cero CVE. La base actualizada
no corrige Express: revisa en `docker scout cves` qué vulnerabilidades altas
vienen de la base y cuáles de las dependencias. Registra digest, arquitectura, fecha y diferencias.

## Práctica 22

**Seguridad**

La referencia es [solutions/security-lab/Dockerfile](../solutions/security-lab/Dockerfile).
Copia tu versión a `material/security-lab/Dockerfile-2` o usa la referencia.
Detén el laboratorio anterior antes de usar su mismo puerto.

```sh
docker build -t security-lab-2 -f solutions/security-lab/Dockerfile material/security-lab
docker run -d --name security-lab-2 --cpus=0.5 --memory=256m --pids-limit=128 --cap-drop=ALL --security-opt=no-new-privileges:true -p 127.0.0.1:8080:8080 security-lab-2
docker exec security-lab-2 id
curl "http://localhost:8080/math?factorize=1%27%3B%20id%20%23"
docker scout quickview security-lab-2
docker rm -f security-lab-2
```
Espera al arranque de Java antes del curl. El UID es 10001. La inyección de comandos
sigue existiendo: se ejecuta con menos privilegios. `nologin` no impide que Java
lance bash. Las flags siguen en la imagen para explicar que un usuario con acceso
al motor puede extraerlas. Corregir la RCE y retirar secretos requiere cambiar el código.

Un usuario no root reduce los privilegios del proceso, pero no convierte el
contenedor en una frontera de seguridad absoluta. Rootless cambia cómo se
ejecuta el motor; `USER` cambia el usuario del proceso dentro del contenedor.

## Práctica 23

**IA (opcional)**

Sigue [la guía de novedades](04-novedades.md). La descarga e inferencia son opcionales.

```sh
docker model pull ai/smollm2:360M-Q4_K_M
docker model run ai/smollm2:360M-Q4_K_M "What is the difference between a Docker image and a container?"
docker model unload ai/smollm2:360M-Q4_K_M
```
La respuesta debe contrastarse con la teoría. No evalúa automáticamente si es correcta.
Para la API, usa el ejemplo con fichero JSON de la guía. No descargues qwen3 sin
comprobar memoria y capacidad de tool calling. El sandbox permite escribir en la
carpeta compartida; no deshace esos cambios al eliminarlo.

Sin Model Runner, lee [examples/ai/tutor.yaml](../examples/ai/tutor.yaml).
El modelo `ai/qwen3` se almacena en Docker Hub (`ai/`) y se descarga con
`docker model pull`. Model Runner genera el texto (`dmr/` en el fichero).
Docker Agent coordina los dos agentes. El ejemplo no tiene herramientas: en
otro caso las aportaría MCP. Docker Sandboxes aislaría el entorno del agente.

## Limpieza final

Para continuar otro día, basta con `docker compose down`.
Solo cuando quieras borrar los datos de los ejercicios:

```sh
docker compose down -v
docker volume rm training-sqlite training-mysql
```
Si un volumen no existe porque saltaste un ejercicio, Docker lo indicará.
No uses `docker system prune` para limpiar un curso en un equipo compartido.

## Comprobación final

Puedes explicar y demostrar estas cinco cosas:

- La diferencia entre `stop`, `start`, `rm` y `run`.
- Por qué editar código no cambia una imagen ya construida.
- Dónde están los datos y qué acción los elimina.
- Por qué `db` funciona desde la aplicación y no desde el navegador.
- Cómo recuperar el servicio sin borrar sus datos.
