# Prácticas del curso

[Índice](../README.md) | [Soluciones](02-soluciones.md)

Las 23 prácticas incluyen enunciados y enlaces a las soluciones, con comandos
y limpieza local. Sigue el orden de cada bloque y consulta las soluciones para
comprobar tus resultados.
Ejecuta desde la raíz del curso. Los comandos de las soluciones van en una línea
para facilitar su uso en Bash/Zsh y PowerShell. Para `curl` en Windows PowerShell
usa `curl.exe`. Los fragmentos de teoría con `\` requieren Bash/Zsh o eliminar
las continuaciones. No copies los símbolos `$` que representan un prompt.

Los ejemplos de consulta son independientes de la secuencia de prácticas.
Antes de una práctica, libera su puerto y sus nombres de contenedor, consultando
`docker ps -a`. Elimina solo los recursos del ejercicio que hayas creado.
Las claves son públicas y didácticas. `docker compose config` puede mostrarlas.

| Práctica | Concepto | Solución |
|---|---|---|
| [1. Ciclo de vida](#práctica-1) | hello-world y un proceso temporal | [Práctica 1](02-soluciones.md#práctica-1) |
| [2. Parámetros de ejecución](#práctica-2) | puertos, etiquetas y configuración de MySQL | [Práctica 2](02-soluciones.md#práctica-2) |
| [3. Salud](#práctica-3) | healthcheck HTTP con cats | [Práctica 3](02-soluciones.md#práctica-3) |
| [4. Capa escribible](#práctica-4) | stop/start frente a eliminar y recrear | [Práctica 4](02-soluciones.md#práctica-4) |
| [5. Volúmenes](#práctica-5) | datos independientes del contenedor | [Práctica 5](02-soluciones.md#práctica-5) |
| [6. Inicialización](#práctica-6) | scripts SQL al crear una base vacía | [Práctica 6](02-soluciones.md#práctica-6) |
| [7. Desarrollo](#práctica-7) | bind mount y recarga automática | [Práctica 7](02-soluciones.md#práctica-7) |
| [8. Persistencia SQLite](#práctica-8) | volumen training-sqlite | [Práctica 8](02-soluciones.md#práctica-8) |
| [9. Primera imagen](#práctica-9) | contexto y Dockerfile | [Práctica 9](02-soluciones.md#práctica-9) |
| [10. Python (opcional)](#práctica-10) | COPY, RUN y EXPOSE | [Práctica 10](02-soluciones.md#práctica-10) |
| [11. Usuario no root (opcional)](#práctica-11) | propiedad de ficheros y USER | [Práctica 11](02-soluciones.md#práctica-11) |
| [12. Multi-stage](#práctica-12) | separar compilación y ejecución | [Práctica 12](02-soluciones.md#práctica-12) |
| [13. Caché](#práctica-13) | reconstruir no cambia contenedores existentes | [Práctica 13](02-soluciones.md#práctica-13) |
| [14. DNS](#práctica-14) | red propia y alias db | [Práctica 14](02-soluciones.md#práctica-14) |
| [15. MySQL para WordPress (opcional)](#práctica-15) | usuario limitado y disponibilidad | [Práctica 15](02-soluciones.md#práctica-15) |
| [16. WordPress (opcional)](#práctica-16) | conexión entre servicios | [Práctica 16](02-soluciones.md#práctica-16) |
| [17. Docker Tasks con MySQL](#práctica-17) | red, credenciales y persistencia | [Práctica 17](02-soluciones.md#práctica-17) |
| [18. WordPress con Compose](#práctica-18) | servicios, volúmenes y healthcheck | [Práctica 18](02-soluciones.md#práctica-18) |
| [19. Docker Tasks con Compose](#práctica-19) | configuración declarativa y recuperación | [Práctica 19](02-soluciones.md#práctica-19) |
| [20. Diagnóstico](#práctica-20) | override con hostname incorrecto | [Práctica 20](02-soluciones.md#práctica-20) |
| [21. Scout](#práctica-21) | CVE de base y dependencias | [Práctica 21](02-soluciones.md#práctica-21) |
| [22. Seguridad](#práctica-22) | reducir privilegios sin corregir la RCE | [Práctica 22](02-soluciones.md#práctica-22) |
| [23. IA (opcional)](#práctica-23) | modelo, inferencia, herramientas y aislamiento | [Práctica 23](02-soluciones.md#práctica-23) |

El bloque de fundamentos incluye las prácticas 1-13; el de redes, Compose,
seguridad e IA incluye las 14-23. Puedes distribuirlos en las sesiones que
necesites o seguirlos a tu ritmo.
Las prácticas opcionales se pueden omitir en el recorrido principal.
La práctica 16 utiliza la base de datos de la práctica 15; hazlas juntas.

## Recursos que se conservan entre prácticas

| Recurso | Se crea en | Se usa en |
|---|---|---|
| Imagen `training-tasks:workshop` | Práctica 8 | Prácticas 13 y 17 |
| Volumen `training-sqlite` | Práctica 8 | Práctica 13 |
| Volumen `training-mysql` | Práctica 17 | Solo práctica 17 |
| Proyecto Compose `training-docker` | Práctica 19 | Práctica 20 |

Compose crea su propia red y su propio volumen; no reutiliza `training-mysql`.
La limpieza final está al final de las [soluciones](02-soluciones.md#limpieza-final).

Continúa con [ampliaciones](05-ampliaciones.md) y el bloque separado de
[novedades de Docker e IA](04-novedades.md).

## Práctica 1

* Ejecuta un contenedor llamado `hello-world` que use la imagen `hello-world`

* Ejecuta un contenedor con las siguientes premisas:
  * El contenedor se llama `timer`
  * El contenedor usa la imagen `ubuntu:24.04`
  * El contenedor es interactivo
  * El contenedor se eliminará tras salir
  * El contenedor ejecuta el comando `sleep 30` (en vez del comando por defecto)

[Solución y limpieza](02-soluciones.md#práctica-1)

## Práctica 2

* Ejecuta un contenedor con las siguientes premisas:
  * El contenedor se llama `nginx` y se ejecuta en *background*
  * El contenedor usa la imagen `nginx:1.30.6-alpine`
  * El contenedor publica su puerto 80 en el puerto 8080 de la máquina local

* Ejecuta un contenedor con las siguientes premisas:
  * El contenedor se llama `practice-db` y se ejecuta en *background*
  * El contenedor tiene una etiqueta con clave `app` y valor `mysql`
  * El contenedor usa la imagen `mysql:9.7.2`
  * El contenedor está configurado para usar la clave de root `secret`
  * El contenedor está configurado para crear automáticamente una base de datos `app`

> Pista: https://hub.docker.com/_/mysql

[Solución y limpieza](02-soluciones.md#práctica-2)

## Práctica 3

* Ejecuta un contenedor con las siguientes premisas:
  * El contenedor se llama `cats` y se ejecuta en *background*
  * El contenedor tiene una etiqueta con clave `app` y valor `cats`
  * El contenedor usa la imagen `mikesir87/cats:1.0`
  * El contenedor publica su puerto 5000 en el puerto local 5050
  * El contenedor tiene un `healthcheck` que usa `curl` para validar que la aplicación está funcionando cada 5 segundos

> Pista: [docker run](https://docs.docker.com/reference/cli/docker/container/run/) incluye las opciones `--health-cmd` y `--health-interval`

* Comprueba con `docker ps` que el contenedor pasa a estado `healthy`

[Solución y limpieza](02-soluciones.md#práctica-3)

## Práctica 4

* Ejecuta en *background* un contenedor `web` con la imagen `nginx:1.30.6-alpine` en el puerto local 8080
* Crea dentro del contenedor el fichero `/usr/share/nginx/html/hello.html` con el texto `Hello`
* Comprueba http://localhost:8080/hello.html
* Para el contenedor, arráncalo de nuevo y comprueba la página
* Elimina el contenedor, crea otro igual y comprueba la página
* Al terminar, elimina `web` para liberar el puerto 8080

¿Qué ocurre en cada caso? ¿Por qué?

> Pista: `docker exec web sh -c "echo Hello > /usr/share/nginx/html/hello.html"`

[Solución y limpieza](02-soluciones.md#práctica-4)

## Práctica 5

* Crea dos volúmenes, uno llamado `volume1` y otro `database-files`

* Ejecuta un contenedor con las siguientes premisas:
  * El contenedor usa la imagen `mysql:9.7.2`
  * El contenedor se llama `persistent-db` y se ejecuta en *background*
  * El contenedor tiene una etiqueta de clave `app` y valor `persistent-db`
  * La contraseña de root es `root` (variable de entorno `MYSQL_ROOT_PASSWORD`)
  * Los ficheros de la base de datos (en la ruta del contenedor `/var/lib/mysql`) se almacenan en el volumen `database-files`

* Elimina el contenedor y comprueba con `docker volume ls` que el volumen sigue existiendo

[Solución y limpieza](02-soluciones.md#práctica-5)

## Práctica 6

* Ejecuta un contenedor con las siguientes premisas:
  * El contenedor usa la imagen `mysql:9.7.2`
  * El contenedor se llama `init-db`
  * Especifica un *bind mount* que comparte la carpeta `material/database-initialization` con el contenedor en `/docker-entrypoint-initdb.d`
  * Establece la variable de entorno `MYSQL_DATABASE` al valor `workshop`
  * Establece la variable de entorno `MYSQL_ROOT_PASSWORD` al valor `secret`
* Espera a que termine la inicialización y consulta la tabla `users` de `workshop`
* Los scripts solo se ejecutan si el directorio de datos está vacío

> La carpeta [database-initialization](../material/database-initialization/README.md) está disponible en el material del curso

[Solución y limpieza](02-soluciones.md#práctica-6)

## Práctica 7

* Ejecuta un contenedor con las siguientes premisas:
  * El contenedor usa la imagen `node:24.22.0-alpine` y se llama `node-app`
  * El contenedor está configurado para ejecutarse interactivamente y para eliminarse cuando se para
  * El contenedor especifica un *bind mount* que conecta la carpeta `material/dev-express` con la carpeta del contenedor `/app`
  * Establece el directorio de trabajo de la aplicación a `/app`
  * Expone el puerto del contenedor 3000 al puerto local 3000
  * Sobrescribe el comando por defecto a `npm run dev`

> Pista: [docker run](https://docs.docker.com/reference/cli/docker/container/run/) incluye la opción `--workdir`

> La carpeta [dev-express](../material/dev-express/README.md) está disponible en el material del curso

Abre http://localhost:3000/api/message

¿Qué ocurre si cambias el mensaje que aparece en `material/dev-express/src/index.js` sin parar el contenedor?

¿Y si haces el mismo cambio en una imagen ya construida?

> En Windows, la recarga solo funciona si el curso está en el sistema de ficheros
> de WSL (por ejemplo `~/curso` en Ubuntu), no en `C:\`. Si no se recarga, para el
> contenedor con Ctrl+C y arráncalo de nuevo.

[Solución y limpieza](02-soluciones.md#práctica-7)

## Práctica 8

La aplicación de tareas del curso guarda los datos en SQLite, en `/data/todo.db`

* Construye la imagen `training-tasks:workshop` a partir de la carpeta `app`
* Crea un volumen llamado `training-sqlite`
* Ejecuta un contenedor con las siguientes premisas:
  * El contenedor se llama `training-app`
  * Publica el puerto 3000 del contenedor en el puerto 8080, solo para tu equipo
  * Monta el volumen `training-sqlite` en `/data`
* Abre http://localhost:8080 y crea una tarea

* Elimina el contenedor `training-app`
* Crea uno nuevo con el mismo comando
* ¿Sigue la tarea? ¿Por qué?
* Repite el experimento **sin** el volumen. ¿Qué ocurre?

Al terminar, libera el puerto 8080 con `docker rm -f training-app`. Conserva el volumen `training-sqlite` hasta el final del curso

[Solución y limpieza](02-soluciones.md#práctica-8)

## Práctica 9

* Crea una imagen llamada `first-build` usando el `Dockerfile` y los contenidos del directorio `material/first-build`
* Ejecuta un contenedor con esa imagen y accede a la página en el puerto local `8080`

> La carpeta [first-build](../material/first-build/README.md) está disponible en el material del curso

* Consulta las capas de la imagen con `docker image history first-build`
* ¿Qué capas son de `nginx` y cuál has creado tú?

[Solución y limpieza](02-soluciones.md#práctica-9)

## Práctica 10

* Completa el `Dockerfile` parcial del directorio `material/simple-python-webapp`
  * Sigue los comentarios `TODO`
  * Una vez completado, construye la imagen con el nombre `simple-python-webapp`
  * Ejecuta el contenedor y accede a la aplicación por el puerto `5000` en tu navegador

> La carpeta [simple-python-webapp](../material/simple-python-webapp/README.md) está disponible en el material del curso

[Solución y limpieza](02-soluciones.md#práctica-10)

## Práctica 11

* Completa el `Dockerfile` parcial del directorio `material/nonroot-node-app`
  * Una vez completado, construye la imagen con el nombre `nonroot-node-app`
  * Ejecuta el contenedor y accede a la aplicación por el puerto `3000` en tu navegador usando el contexto `/api/message`
  * Comprueba con `docker exec` que el proceso **no** se ejecuta como `root`

> Pista: crea un directorio propiedad de `app-user` y usa `COPY --chown`. `USER` no cambia permisos de directorios existentes

[Solución y limpieza](02-soluciones.md#práctica-11)

## Práctica 12

* Completa el `Dockerfile` parcial del directorio `material/multi-stage-react-app`
  * Añade una segunda etapa basada en `nginx:1.30.6-alpine`
  * Copia los ficheros construidos en la primera etapa (`/usr/local/app/dist`) a `/usr/share/nginx/html`
  * Construye la imagen con el nombre `multi-stage-react-app`
  * Ejecuta el contenedor y accede a la aplicación por el puerto local `8080`
* Compara el tamaño de la imagen con el de `node:24.22.0-alpine` usando `docker image ls` (columna `DISK USAGE` en Docker Desktop)

[Solución y limpieza](02-soluciones.md#práctica-12)

## Práctica 13

Arranca `training-app` con `training-tasks:workshop`, el volumen `training-sqlite` en `/data`
y el puerto local 8080, como en la práctica 8, antes de modificar el archivo.

* En `app/src/static/index.html`, cambia el encabezado `Docker Tasks` por `My Docker Tasks`
* Construye la imagen `training-tasks:v2` con `--progress=plain`
  * ¿Qué pasos aparecen como `CACHED`?
* Recarga el navegador. ¿Ha cambiado el título? ¿Por qué?
* Recrea el contenedor `training-app` con la nueva imagen y el volumen `training-sqlite`
* Restaura el encabezado original al terminar

¿Qué ocurriría si `COPY src` estuviese antes de `RUN npm ci`?

[Solución y limpieza](02-soluciones.md#práctica-13)

## Práctica 14

* Crea una red llamada `getting-started`

* Ejecuta un contenedor con las siguientes premisas:
  * El contenedor usa la imagen `mysql:9.7.2`
  * El contenedor tiene el nombre `networked-db`
  * El contenedor está configurado para usar la clave de root `secret`
  * El contenedor está configurado para crear automáticamente una base de datos `app`
  * El contenedor está conectado a la red `getting-started`
  * El contenedor usa el alias de red `db`
* Comprueba con `busybox:1.37` que el nombre `db` se resuelve en esa red

> Pista: https://hub.docker.com/_/mysql

[Solución y limpieza](02-soluciones.md#práctica-14)

## Práctica 15

* Crea una red llamada `wordpress`

* Ejecuta un contenedor con las siguientes premisas:
  * El contenedor usa la imagen `mysql:9.7.2`
  * El contenedor está conectado a la red `wordpress`
  * El contenedor usa el alias de red `db`
  * El contenedor está configurado para usar la clave de root `secret`
  * El contenedor crea la base `wordpress` y el usuario `manager` con clave didáctica `secret`

[Solución y limpieza](02-soluciones.md#práctica-15)

## Práctica 16

* Ejecuta un contenedor con las siguientes premisas:
  * El contenedor usa la imagen `wordpress:7.1.3-apache`
  * El contenedor publica su puerto 80 en el puerto 8080 local
  * El contenedor está conectado a la red `wordpress`
  * El contenedor usa la base de datos `wordpress` del contenedor MySQL anterior, con el usuario `manager`
* Abre http://localhost:8080 y completa la instalación

> Pista: https://hub.docker.com/_/wordpress

* Elimina los contenedores y la red al terminar

[Solución y limpieza](02-soluciones.md#práctica-16)

## Práctica 17

* Crea la red `training-net` y el volumen `training-mysql`
* Ejecuta MySQL con las siguientes premisas:
  * Nombre `training-db`, imagen `mysql:9.7.2`, red `training-net`, alias `db`
  * Contraseña de root aleatoria (`MYSQL_RANDOM_ROOT_PASSWORD=yes`)
  * Base de datos `tasks`, usuario `tasks`, contraseña `classroom-only`
  * Datos en el volumen `training-mysql`
* Ejecuta `training-app` en la red `training-net`, en el puerto 8080 de tu equipo, con las variables `MYSQL_HOST=db`, `MYSQL_USER`, `MYSQL_PASSWORD` y `MYSQL_DB`

> Espera a que MySQL termine de inicializarse: revisa `docker logs training-db`

* Crea una tarea en http://localhost:8080
* Consulta la tabla desde MySQL:

```sh
docker exec -e MYSQL_PWD=classroom-only training-db mysql -u tasks -D tasks -e "SELECT name FROM todo_items"
```

* ¿Por qué `db` funciona desde `training-app` y no desde tu navegador?
* ¿Por qué no hemos publicado el puerto 3306?
* ¿Qué pasaría si `MYSQL_HOST` fuese `localhost`?

Limpieza: `docker rm -f training-app training-db` y `docker network rm training-net`

[Solución y limpieza](02-soluciones.md#práctica-17)

## Práctica 18

* Crea una plantilla `compose.yaml` en una carpeta nueva `wordpress-compose` que incluya los siguientes contenedores

```bash
docker run -d --network wordpress --name wp-db -e MYSQL_ROOT_PASSWORD=secret -e MYSQL_DATABASE=wordpress \
  -e MYSQL_USER=manager -e MYSQL_PASSWORD=secret \
  -v mysql-data:/var/lib/mysql --network-alias db mysql:9.7.2

docker run -d --network wordpress --name wp -p 127.0.0.1:8080:80 \
  -e WORDPRESS_DB_HOST=db -e WORDPRESS_DB_NAME=wordpress \
  -e WORDPRESS_DB_USER=manager -e WORDPRESS_DB_PASSWORD=secret \
  -v wordpress-data:/var/www/html wordpress:7.1.3-apache
```

* Ejecuta Docker Compose y verifica que WordPress funciona en http://localhost:8080
* Añade un `healthcheck` SQL a `db` y usa `condition: service_healthy`
* Para probarlos manualmente: crea antes la red `wordpress` y espera a MySQL. No los ejecutes junto con Compose

> Pista: https://www.composerize.com convierte `docker run` en Compose. Para el
> `healthcheck`, adapta el de `db` en `compose.yaml` (`CMD-SHELL` y `SELECT 1`).
> En Compose, `$$` escribe un `$` literal.

* ¿Por qué no necesitas `--network-alias db` en Compose?
* ¿Qué ocurre con los datos tras `docker compose down`? ¿Y tras `docker compose down -v`?
* ¿Por qué no hace falta publicar el puerto de MySQL?

[Solución y limpieza](02-soluciones.md#práctica-18)

## Práctica 19

* Abre [compose.yaml](../compose.yaml) en la raíz del repositorio
  * Identifica servicios, red, volumen, `healthcheck` y `depends_on`
  * `build:` construye la imagen desde una carpeta; `image:` la descarga de un registro
* Arranca el proyecto y espera a que esté sano
* Crea una tarea en http://localhost:8080
* Para y elimina el proyecto **sin** borrar el volumen, arráncalo de nuevo y comprueba la tarea
* Extra: cambia el puerto a 8081 usando un fichero `.env`, sin editar `compose.yaml`

> Pista: `cp .env.example .env` (en PowerShell, `Copy-Item .env.example .env`) y
> cambia el puerto a 8081

[Solución y limpieza](02-soluciones.md#práctica-19)

## Práctica 20

El fichero `examples/compose.failure.yaml` introduce un error de configuración

```sh
docker compose -f compose.yaml -f examples/compose.failure.yaml up -d
```

* Espera unos 15 segundos: al principio `app` aparece como `health: starting`
* Diagnostica el problema con `docker compose ps -a` y `docker compose logs app`
* Usa `config` con los mismos dos argumentos `-f` para encontrar la causa
* Recupera el servicio **sin borrar los datos**

¿Por qué reconstruir la imagen no arregla el problema?

[Solución y limpieza](02-soluciones.md#práctica-20)

## Práctica 21

* Construye la imagen `demo-service` a partir de `material/scout-demo`
* Analízala con `docker scout quickview`
* Modifica el `Dockerfile` aplicando la recomendación de imagen base (versión LTS de Node.js)
* Construye la Imagen Docker de nuevo
* Compara los resultados; actualizar no garantiza cero vulnerabilidades
* Extra: ¿qué vulnerabilidades altas quedan? ¿De dónde vienen?

[Solución y limpieza](02-soluciones.md#práctica-21)

## Práctica 22

Sigue el [laboratorio de seguridad](../material/security-lab/README.md) para
construir y probar la imagen inicial y observar la inyección de comandos.

* Escribe `material/security-lab/Dockerfile-2` a partir de `Dockerfile-1`
  * El contenedor se ejecuta con un usuario sin privilegios
  * No hay `bash` con *setuid* ni herramientas de red adicionales
* Construye la imagen `security-lab-2`
* Ejecútala limitando CPU a `0.5` y memoria a `256m`
* Repite el ataque: ¿qué usuario aparece ahora?
* Compara las dos imágenes con `docker scout quickview`

> [Solución](../solutions/security-lab/Dockerfile)

[Solución y limpieza](02-soluciones.md#práctica-22)

## Práctica 23

Si tu equipo cumple los requisitos de Model Runner:

* Descarga `ai/smollm2:360M-Q4_K_M` y pregúntale "What is the difference between a Docker image and a container?"
* Compara la respuesta con lo aprendido. ¿Es correcta?
* Llama a la misma pregunta mediante la API con `curl`
* Libera la memoria con `docker model unload`

Si no:

* Lee `examples/ai/tutor.yaml` y explica qué pieza hace cada tarea: almacenar el modelo, generar texto, invocar una herramienta o aislar el entorno

> [Guía completa de novedades](04-novedades.md)

[Solución y limpieza](02-soluciones.md#práctica-23)
