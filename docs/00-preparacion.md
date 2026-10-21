# Preparar el entorno

[Volver al índice](../README.md)

No necesitas conocer Docker. Antes de empezar, prepara un equipo con Docker,
navegador, terminal y editor de texto plano. No hacen falta Node.js, MySQL ni un
IDE para realizar las prácticas.

## Según tu sistema

| Sistema | Entorno del curso |
|---|---|
| Windows | Docker Desktop con backend WSL2 y contenedores Linux. PowerShell o terminal WSL. |
| macOS | Docker Desktop para tu procesador: Apple Silicon o Intel. Terminal con Zsh/Bash. |
| Linux | Docker Engine con plugin Compose, o Docker Desktop. Terminal Bash. |

Sigue la [instalación oficial](https://docs.docker.com/get-started/get-docker/).
En Windows, no cambies entre PowerShell y WSL a mitad de un ejercicio con rutas.
Si utilizas WSL, guarda el proyecto en su sistema de archivos Linux.
Con el backend WSL 2, la memoria y las CPU de Docker se configuran en
`%UserProfile%\.wslconfig`, no en *Settings* de Docker Desktop.
Usa una carpeta local sencilla, fuera de carpetas sincronizadas.

En Mac con Apple Silicon puedes elegir la máquina virtual en *Settings > General >
Virtual Machine Manager*: [Docker VMM](https://docs.docker.com/desktop/features/vmm/)
o Apple Virtualization framework. Las dos sirven para el curso. Docker VMM arranca
más rápido, pero no admite Rosetta, así que emular imágenes `amd64` es más lento.
Si un *bind mount* falla con "file is not shared from the host", añade la carpeta
en *Settings > Resources > File sharing*.

En Linux, verifica que tu usuario puede conectar con el motor. La pertenencia al
grupo `docker` concede privilegios elevados sobre ese equipo; consulta las
[opciones de instalación](https://docs.docker.com/engine/install/linux-postinstall/)
o [rootless](https://docs.docker.com/engine/security/rootless/).

## Comprobación obligatoria

Inicia Docker Desktop si lo utilizas. Ejecuta cada línea:

```sh
docker version
docker compose version
docker run --rm hello-world
```

Resultado: `docker version` muestra **Client y Server** sin error; Compose muestra
su versión y el último comando imprime `Hello from Docker!`.
Que exista el comando `docker` no demuestra que el motor esté funcionando.

El laboratorio usa la CLI actual `docker compose`, no `docker-compose`.
Los ejemplos Watch necesitan Compose 2.23 o posterior. Versiones principales
posteriores también sirven; no interpretes "Compose v2" como un número obligatorio.

## Descargar y preparar

Clona el repositorio del curso desde GitHub con Git o GitHub Desktop. Usa la URL
del botón `Code` del repositorio que vayas a utilizar.
Abre la terminal en la carpeta del material y comprueba con `pwd` que estás junto
a `compose.yaml`. Si trabajas con el workspace de preparación, entra en `course/`.

```sh
docker pull node:24.22.0-trixie-slim
docker pull mysql:9.7.2
docker build -t training-tasks:workshop ./app
docker run --rm --name training-preflight -d -p 127.0.0.1:18080:3000 training-tasks:workshop
```

Abre http://localhost:18080. Si ves Docker Tasks, termina la comprobación:

```sh
docker stop training-preflight
```

El contenedor se elimina automáticamente por `--rm`. La imagen queda preparada.
Conserva esa imagen y esta carpeta mientras realizas las prácticas.

Para reducir las esperas durante los ejercicios, descarga sus imágenes:

```sh
docker pull hello-world
docker pull ubuntu:24.04
docker pull nginx:1.30.6-alpine
docker pull mikesir87/cats:1.0
docker pull node:24.22.0-alpine
docker pull python:3.13.16-alpine
docker pull busybox:1.37
docker pull wordpress:7.1.3-apache
docker pull node:18-alpine
docker pull maven:3.10.0-eclipse-temurin-21-noble
docker pull eclipse-temurin:21.0.12.1_1-jre-noble
```

`node:18-alpine` es antigua a propósito: la práctica 21 analiza sus vulnerabilidades.

Si una descarga falla, comprueba VPN, proxy y acceso a Docker Hub antes de continuar.
Si 18080 está ocupado, usa 18081 en el comando y en el navegador.
No es necesario descargar modelos de IA: sus requisitos son independientes.

## Convenciones de los ejemplos

En los ejemplos, `abc`, `<id>`, `<imagen>`, `<digest>`, `tuusuario` y las rutas
inventadas son marcadores que debes sustituir. Las salidas con `$` representan
una terminal: no copies el prompt. Los YAML parciales explican una propiedad;
los archivos completos ejecutables están en `examples/` y `compose.yaml`.
No ejecutes `docker init` sobre el material del curso;
pruébalo en una copia de un proyecto de ejemplo.

Para Compose Include local se requiere Compose 2.20+; `sync+restart` requiere
2.23+; `models`, 2.38+. Utiliza una versión mantenida y comprueba `docker compose config`.
