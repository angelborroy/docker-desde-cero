# Prácticas del curso

[Índice](../README.md) | [Soluciones](02-soluciones.md)

Esta guía contiene los enunciados completos de las 23 prácticas, sus requisitos,
la comprobación del resultado y la limpieza. Si sigues una sesión, mantén el
índice abierto y sigue el número de práctica indicado por el profesor. Lee el
enunciado en GitHub y trabaja en tu copia local con el editor y la terminal.
Consulta las soluciones después de intentarlo para contrastar tu razonamiento.
Ejecuta desde la raíz del curso. Los comandos de las soluciones van en una línea
para facilitar su uso en Bash/Zsh y PowerShell. Para `curl` en Windows PowerShell
usa `curl.exe`. Los fragmentos de teoría con `\` requieren Bash/Zsh o eliminar
las continuaciones. No copies los símbolos `$` que representan un prompt.

Los ejemplos de consulta son independientes de la secuencia de prácticas.
Antes de una práctica, libera su puerto y sus nombres de contenedor, consultando
`docker ps -a`. Elimina solo los recursos del ejercicio que hayas creado.
En las limpiezas, sustituye `<ID>` por el identificador de tu contenedor, obtenido
con `docker ps -a`. Los recursos que se conservan se indican en cada práctica.
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
| Contenedor `wp-db` y red `wordpress` | Práctica 15 | Práctica 16 (ambas opcionales) |
| Volumen `training-mysql` | Práctica 17 | Solo práctica 17 |
| Proyecto Compose `training-docker` | Práctica 19 | Práctica 20 |

Compose crea su propia red y su propio volumen; no reutiliza `training-mysql`.
La [limpieza final](#limpieza-final) está al final de esta guía.

Continúa con [ampliaciones](05-ampliaciones.md) y el bloque separado de
[novedades de Docker e IA](04-novedades.md).

## Práctica 1

**Ciclo de vida**

**Antes de empezar:** Docker iniciado; no necesitas recursos de otras prácticas.

* Ejecuta un contenedor llamado `hello-world` que use la imagen `hello-world`

* Ejecuta un contenedor con las siguientes premisas:
  * El contenedor se llama `timer`
  * El contenedor usa la imagen `ubuntu:24.04`
  * El contenedor es interactivo
  * El contenedor se eliminará tras salir
  * El contenedor ejecuta el comando `sleep 30` (en vez del comando por defecto)

**Comprueba el resultado:** Localiza `hello-world` y `timer` con `docker ps -a` tras finalizar ambos procesos y explica la diferencia.

**Limpieza y continuidad:** Elimina `hello-world` con `docker rm hello-world`. `timer` se elimina al terminar gracias a `--rm`.

[Consultar solución](02-soluciones.md#práctica-1)

## Práctica 2

**Parámetros de ejecución**

**Antes de empezar:** Puerto 8080 libre; no necesitas recursos de otras prácticas.

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

**Comprueba el resultado:** Abre http://localhost:8080 y comprueba con `docker inspect practice-db` la etiqueta y las variables solicitadas.

**Limpieza y continuidad:** Ejecuta `docker rm -fv nginx practice-db` para liberar el puerto y borrar sus volúmenes anónimos.

[Consultar solución](02-soluciones.md#práctica-2)

## Práctica 3

**Salud**

**Antes de empezar:** Puerto 5050 libre; no necesitas recursos de otras prácticas.

* Ejecuta un contenedor con las siguientes premisas:
  * El contenedor se llama `cats` y se ejecuta en *background*
  * El contenedor tiene una etiqueta con clave `app` y valor `cats`
  * El contenedor usa la imagen `mikesir87/cats:1.0`
  * El contenedor publica su puerto 5000 en el puerto local 5050
  * El contenedor tiene un `healthcheck` que usa `curl` para validar que la aplicación está funcionando cada 5 segundos

> Pista: [docker run](https://docs.docker.com/reference/cli/docker/container/run/) incluye las opciones `--health-cmd` y `--health-interval`

* Comprueba con `docker ps` que el contenedor pasa a estado `healthy`

**Comprueba el resultado:** La página http://localhost:5050 responde y `docker ps` muestra `healthy` después de las primeras comprobaciones.

**Limpieza y continuidad:** Ejecuta `docker rm -f cats`.

[Consultar solución](02-soluciones.md#práctica-3)

## Práctica 4

**Capa escribible**

**Antes de empezar:** Puerto 8080 libre; no necesitas recursos de otras prácticas.

* Ejecuta en *background* un contenedor `web` con la imagen `nginx:1.30.6-alpine` en el puerto local 8080
* Crea dentro del contenedor el fichero `/usr/share/nginx/html/hello.html` con el texto `Hello`
* Comprueba http://localhost:8080/hello.html
* Para el contenedor, arráncalo de nuevo y comprueba la página
* Elimina el contenedor, crea otro igual y comprueba la página

¿Qué ocurre en cada caso? ¿Por qué?

> Pista: `docker exec web sh -c "echo Hello > /usr/share/nginx/html/hello.html"`

**Comprueba el resultado:** Anota si `hello.html` existe tras cada operación y relaciona el resultado con la capa escribible.

**Limpieza y continuidad:** Ejecuta `docker rm -f web` para liberar el puerto 8080.

[Consultar solución](02-soluciones.md#práctica-4)

## Práctica 5

**Volúmenes**

**Antes de empezar:** No necesitas recursos de otras prácticas.

* Crea dos volúmenes, uno llamado `volume1` y otro `database-files`

* Ejecuta un contenedor con las siguientes premisas:
  * El contenedor usa la imagen `mysql:9.7.2`
  * El contenedor se llama `persistent-db` y se ejecuta en *background*
  * El contenedor tiene una etiqueta de clave `app` y valor `persistent-db`
  * La contraseña de root es `root` (variable de entorno `MYSQL_ROOT_PASSWORD`)
  * Los ficheros de la base de datos (en la ruta del contenedor `/var/lib/mysql`) se almacenan en el volumen `database-files`

* Elimina el contenedor y comprueba con `docker volume ls` que el volumen sigue existiendo

**Comprueba el resultado:** Tras eliminar `persistent-db`, localiza `database-files` con `docker volume ls`.

**Limpieza y continuidad:** Si aún existe, elimina `persistent-db` con `docker rm -f persistent-db`. Después, borra solo estos volúmenes de prueba con `docker volume rm volume1 database-files`.

[Consultar solución](02-soluciones.md#práctica-5)

## Práctica 6

**Inicialización**

**Antes de empezar:** Copia local del repositorio con la carpeta `material/database-initialization`; no necesitas recursos de otras prácticas.

* Ejecuta un contenedor con las siguientes premisas:
  * El contenedor usa la imagen `mysql:9.7.2`
  * El contenedor se llama `init-db`
  * Especifica un *bind mount* que comparte la carpeta `material/database-initialization` con el contenedor en `/docker-entrypoint-initdb.d`
  * Establece la variable de entorno `MYSQL_DATABASE` al valor `workshop`
  * Establece la variable de entorno `MYSQL_ROOT_PASSWORD` al valor `secret`
* Espera a que termine la inicialización y consulta la tabla `users` de `workshop`
* Los scripts solo se ejecutan si el directorio de datos está vacío

> La carpeta [database-initialization](../material/database-initialization/README.md) está disponible en el material del curso

**Comprueba el resultado:** La consulta a `workshop.users` devuelve Moby Dock y Whale Watcher una vez terminada la inicialización.

**Limpieza y continuidad:** Ejecuta `docker rm -fv init-db` para eliminar el contenedor y su volumen anónimo.

[Consultar solución](02-soluciones.md#práctica-6)

## Práctica 7

**Desarrollo**

**Antes de empezar:** Copia local de `material/dev-express` y puerto 3000 libre. Lee la nota de WSL antes de empezar si usas Windows.

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

**Comprueba el resultado:** La respuesta de `/api/message` refleja el mensaje editado; si no hay recarga automática, aplica la alternativa indicada para Windows.

**Limpieza y continuidad:** Termina con Ctrl+C; `--rm` elimina `node-app`. Restaura el mensaje original en el fichero que has editado.

[Consultar solución](02-soluciones.md#práctica-7)

## Práctica 8

**Persistencia SQLite**

**Antes de empezar:** Copia local de `app` y puerto 8080 libre. Esta práctica crea los recursos que usarás en las prácticas 13 y 17.

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

**Comprueba el resultado:** Compara si la tarea permanece al recrear el contenedor con volumen y sin él.

**Limpieza y continuidad:** Ejecuta `docker rm -f training-app`. Conserva la imagen `training-tasks:workshop` para las prácticas 13 y 17 y el volumen `training-sqlite` hasta el final del curso.

[Consultar solución](02-soluciones.md#práctica-8)

## Práctica 9

**Primera imagen**

**Antes de empezar:** Copia local de `material/first-build` y puerto 8080 libre.

* Crea una imagen llamada `first-build` usando el `Dockerfile` y los contenidos del directorio `material/first-build`
* Ejecuta un contenedor con esa imagen y accede a la página en el puerto local `8080`

> La carpeta [first-build](../material/first-build/README.md) está disponible en el material del curso

* Consulta las capas de la imagen con `docker image history first-build`
* ¿Qué capas son de `nginx` y cuál has creado tú?

**Comprueba el resultado:** La página responde en http://localhost:8080 y puedes identificar la incorporación del sitio en el historial de la imagen.

**Limpieza y continuidad:** Si lo ejecutaste en primer plano con `--rm`, termina con Ctrl+C. En otro caso, identifica tu contenedor con `docker ps -a` y elimínalo con `docker rm -f <ID>` para liberar 8080.

[Consultar solución](02-soluciones.md#práctica-9)

## Práctica 10

**Python (opcional)**

**Antes de empezar:** Copia local de `material/simple-python-webapp` y puerto 5000 libre. Si está ocupado, utiliza 5051 como puerto local.

* Completa el `Dockerfile` parcial del directorio `material/simple-python-webapp`
  * Sigue los comentarios `TODO`
  * Una vez completado, construye la imagen con el nombre `simple-python-webapp`
  * Ejecuta el contenedor y accede a la aplicación por el puerto `5000` en tu navegador

> La carpeta [simple-python-webapp](../material/simple-python-webapp/README.md) está disponible en el material del curso

**Comprueba el resultado:** La aplicación responde en http://localhost:5000, o en el puerto alternativo que hayas publicado.

**Limpieza y continuidad:** Si lo ejecutaste con `--rm`, termina con Ctrl+C. En otro caso, elimina el contenedor de esta práctica con `docker rm -f <ID>`. Conserva tu Dockerfile como trabajo realizado.

[Consultar solución](02-soluciones.md#práctica-10)

## Práctica 11

**Usuario no root (opcional)**

**Antes de empezar:** Copia local de `material/nonroot-node-app` y puerto 3000 libre.

* Completa el `Dockerfile` parcial del directorio `material/nonroot-node-app`
  * Una vez completado, construye la imagen con el nombre `nonroot-node-app`
  * Ejecuta el contenedor y accede a la aplicación por el puerto `3000` en tu navegador usando el contexto `/api/message`
  * Comprueba con `docker exec` que el proceso **no** se ejecuta como `root`

> Pista: crea un directorio propiedad de `app-user` y usa `COPY --chown`. `USER` no cambia permisos de directorios existentes

**Comprueba el resultado:** http://localhost:3000/api/message responde y `id` dentro del contenedor muestra un UID distinto de 0.

**Limpieza y continuidad:** Elimina el contenedor de esta práctica con `docker rm -f <ID>`; si lo llamaste `nonroot`, usa `docker rm -f nonroot`. Conserva tu Dockerfile.

[Consultar solución](02-soluciones.md#práctica-11)

## Práctica 12

**Multi-stage**

**Antes de empezar:** Copia local de `material/multi-stage-react-app` y puerto 8080 libre.

* Completa el `Dockerfile` parcial del directorio `material/multi-stage-react-app`
  * Añade una segunda etapa basada en `nginx:1.30.6-alpine`
  * Copia los ficheros construidos en la primera etapa (`/usr/local/app/dist`) a `/usr/share/nginx/html`
  * Construye la imagen con el nombre `multi-stage-react-app`
  * Ejecuta el contenedor y accede a la aplicación por el puerto local `8080`
* Compara el tamaño de la imagen con el de `node:24.22.0-alpine` usando `docker image ls` (columna `DISK USAGE` en Docker Desktop)

**Comprueba el resultado:** La aplicación responde en http://localhost:8080; compara el tamaño de la imagen final y los componentes que contiene.

**Limpieza y continuidad:** Si lo ejecutaste con `--rm`, termina con Ctrl+C. En otro caso, elimina tu contenedor con `docker rm -f <ID>` para liberar 8080. Conserva tu Dockerfile.

[Consultar solución](02-soluciones.md#práctica-12)

## Práctica 13

**Caché**

**Antes de empezar:** Imagen `training-tasks:workshop`, volumen `training-sqlite` y una tarea de la práctica 8; puerto 8080 libre. Si te faltan, completa primero la práctica 8.

Arranca `training-app` con `training-tasks:workshop`, el volumen `training-sqlite` en `/data`
y el puerto local 8080, como en la práctica 8, antes de modificar el archivo.

* En `app/src/static/index.html`, cambia el encabezado `Docker Tasks` por `My Docker Tasks`
* Construye la imagen `training-tasks:v2` con `--progress=plain`
  * ¿Qué pasos aparecen como `CACHED`?
* Recarga el navegador. ¿Ha cambiado el título? ¿Por qué?
* Recrea el contenedor `training-app` con la nueva imagen y el volumen `training-sqlite`
* Restaura el encabezado original al terminar

¿Qué ocurriría si `COPY src` estuviese antes de `RUN npm ci`?

**Comprueba el resultado:** El título cambia al recrear el contenedor y la tarea del volumen se conserva. Identifica los pasos marcados como `CACHED`.

**Limpieza y continuidad:** Restaura `Docker Tasks` en `app/src/static/index.html`, elimina `training-app` con `docker rm -f training-app` y reconstruye `training-tasks:workshop` con `docker build -t training-tasks:workshop ./app`. Conserva esa imagen y `training-sqlite`.

[Consultar solución](02-soluciones.md#práctica-13)

## Práctica 14

**DNS**

**Antes de empezar:** No necesitas recursos de otras prácticas; la red `getting-started` se crea aquí.

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

**Comprueba el resultado:** La consulta DNS desde BusyBox devuelve la dirección de `db` dentro de `getting-started`.

**Limpieza y continuidad:** Ejecuta `docker rm -fv networked-db` y después `docker network rm getting-started`.

[Consultar solución](02-soluciones.md#práctica-14)

## Práctica 15

**MySQL para WordPress (opcional)**

**Antes de empezar:** No necesitas recursos de otras prácticas. Haz esta práctica opcional junto con la 16.

* Crea una red llamada `wordpress`

* Ejecuta un contenedor con las siguientes premisas:
  * El contenedor usa la imagen `mysql:9.7.2`
  * El contenedor se llama `wp-db`
  * El contenedor está conectado a la red `wordpress`
  * El contenedor usa el alias de red `db`
  * El contenedor está configurado para usar la clave de root `secret`
  * El contenedor crea la base `wordpress` y el usuario `manager` con clave didáctica `secret`

**Comprueba el resultado:** Espera a que MySQL acepte una consulta `SELECT 1` con el usuario `manager` sobre la base `wordpress`.

**Limpieza y continuidad:** Conserva `wp-db` y la red `wordpress` para la práctica 16. Si no vas a continuar, ejecuta `docker rm -fv wp-db` y `docker network rm wordpress`.

[Consultar solución](02-soluciones.md#práctica-15)

## Práctica 16

**WordPress (opcional)**

**Antes de empezar:** Práctica 15 completada: contenedor `wp-db` listo y red `wordpress`; puerto 8080 libre.

* Ejecuta un contenedor con las siguientes premisas:
  * El contenedor usa la imagen `wordpress:7.1.3-apache` y se llama `wp`
  * El contenedor publica su puerto 80 en el puerto 8080 local
  * El contenedor está conectado a la red `wordpress`
  * El contenedor usa la base de datos `wordpress` del contenedor MySQL anterior, con el usuario `manager`
* Abre http://localhost:8080 y completa la instalación

> Pista: https://hub.docker.com/_/wordpress

**Comprueba el resultado:** Abre http://localhost:8080 y completa la instalación de WordPress.

**Limpieza y continuidad:** Ejecuta `docker rm -fv wp wp-db` y `docker network rm wordpress`. Estos datos de prueba no se reutilizan en Compose.

[Consultar solución](02-soluciones.md#práctica-16)

## Práctica 17

**Docker Tasks con MySQL**

**Antes de empezar:** Imagen `training-tasks:workshop` de la práctica 8 y puerto 8080 libre. Si te falta la imagen, ejecuta `docker build -t training-tasks:workshop ./app`.

* Crea la red `training-net` y el volumen `training-mysql`
* Ejecuta MySQL con las siguientes premisas:
  * Nombre `training-db`, imagen `mysql:9.7.2`, red `training-net`, alias `db`
  * Contraseña de root aleatoria (`MYSQL_RANDOM_ROOT_PASSWORD=yes`)
  * Base de datos `tasks`, usuario `tasks`, contraseña `classroom-only`
  * Datos en el volumen `training-mysql`
* Ejecuta `training-app` con la imagen `training-tasks:workshop` en la red `training-net`, en el puerto 8080 de tu equipo, con las variables `MYSQL_HOST=db`, `MYSQL_USER`, `MYSQL_PASSWORD` y `MYSQL_DB`

> Espera a que MySQL termine de inicializarse: revisa `docker logs training-db`

* Crea una tarea en http://localhost:8080
* Consulta la tabla desde MySQL:

```sh
docker exec -e MYSQL_PWD=classroom-only training-db mysql -u tasks -D tasks -e "SELECT name FROM todo_items"
```

* ¿Por qué `db` funciona desde `training-app` y no desde tu navegador?
* ¿Por qué no hemos publicado el puerto 3306?
* ¿Qué pasaría si `MYSQL_HOST` fuese `localhost`?

**Comprueba el resultado:** La tarea creada en la web aparece en la consulta SQL a `todo_items`.

**Limpieza y continuidad:** Ejecuta `docker rm -f training-app training-db` y `docker network rm training-net`. Conserva `training-mysql` hasta la limpieza final; Compose utilizará un volumen distinto.

[Consultar solución](02-soluciones.md#práctica-17)

## Práctica 18

**WordPress con Compose**

**Antes de empezar:** Puerto 8080 libre y carpeta nueva `wordpress-compose`. No necesitas completar las prácticas opcionales 15 y 16; si las hiciste, termina su limpieza.

* Crea una plantilla `compose.yaml` en una carpeta nueva `wordpress-compose` que incluya los siguientes contenedores

```bash
docker run -d --network wordpress --name wp-db -e MYSQL_ROOT_PASSWORD=secret -e MYSQL_DATABASE=wordpress \
  -e MYSQL_USER=manager -e MYSQL_PASSWORD=secret \
  -v wp-mysql-data:/var/lib/mysql --network-alias db mysql:9.7.2

docker run -d --network wordpress --name wp -p 127.0.0.1:8080:80 \
  -e WORDPRESS_DB_HOST=db -e WORDPRESS_DB_NAME=wordpress \
  -e WORDPRESS_DB_USER=manager -e WORDPRESS_DB_PASSWORD=secret \
  -v wp-html-data:/var/www/html wordpress:7.1.3-apache
```

* Ejecuta Docker Compose y verifica que WordPress funciona en http://localhost:8080
* Añade un `healthcheck` SQL a `db` y usa `condition: service_healthy`
* Para probarlos manualmente: crea antes la red `wordpress` y espera a MySQL.
  En PowerShell, escribe cada comando en una línea, sin `\`.
  Antes de pasar a Compose, elimina esos contenedores con `docker rm -f wp wp-db`,
  la red con `docker network rm wordpress` y sus volúmenes de prueba con
  `docker volume rm wp-mysql-data wp-html-data`. No los ejecutes junto con Compose

> Pista: https://www.composerize.com convierte `docker run` en Compose. Para el
> `healthcheck`, adapta el de `db` en `compose.yaml` (`CMD-SHELL` y `SELECT 1`).
> En Compose, `$$` escribe un `$` literal.

* ¿Por qué no necesitas `--network-alias db` en Compose?
* ¿Qué ocurre con los datos tras `docker compose down`? ¿Y tras `docker compose down -v`?
* ¿Por qué no hace falta publicar el puerto de MySQL?

**Comprueba el resultado:** WordPress responde en http://localhost:8080 y su arranque espera a que la consulta del healthcheck de MySQL funcione.

**Limpieza y continuidad:** Desde `wordpress-compose`, ejecuta `docker compose down -v` al terminar la comparación para borrar solo los datos de este ejercicio; después vuelve a la raíz del repositorio. Si probaste la referencia desde la raíz, usa `docker compose -f examples/compose.wordpress.yaml down -v`.

[Consultar solución](02-soluciones.md#práctica-18)

## Práctica 19

**Docker Tasks con Compose**

**Antes de empezar:** Raíz del repositorio y puerto 8080 libre. No necesitas los recursos de la práctica 17; si la hiciste, elimina sus contenedores antes de empezar.

* Abre [compose.yaml](../compose.yaml) en la raíz del repositorio
  * Identifica servicios, red, volumen, `healthcheck` y `depends_on`
  * `build:` construye la imagen desde una carpeta; `image:` la descarga de un registro
* Arranca el proyecto y espera a que esté sano
* Crea una tarea en http://localhost:8080
* Para y elimina el proyecto **sin** borrar el volumen, arráncalo de nuevo y comprueba la tarea
* Extra: cambia el puerto a 8081 usando un fichero `.env`, sin editar `compose.yaml`

> Pista: `cp .env.example .env` (en PowerShell, `Copy-Item .env.example .env`) y
> cambia el puerto a 8081

**Comprueba el resultado:** Los servicios están saludables y la tarea permanece después de eliminar y volver a crear el proyecto sin borrar el volumen.

**Limpieza y continuidad:** Si hiciste el extra, restaura `APP_PORT=8080` en `.env` y aplica el cambio con `docker compose up -d --wait`. Conserva el proyecto y sus datos para la práctica 20. Si haces una pausa, puedes usar `docker compose down` sin `-v`.

[Consultar solución](02-soluciones.md#práctica-19)

## Práctica 20

**Diagnóstico**

**Antes de empezar:** Práctica 19 completada, con una tarea guardada. Trabaja desde la raíz del repositorio.

El fichero `examples/compose.failure.yaml` introduce un error de configuración

```sh
docker compose -f compose.yaml -f examples/compose.failure.yaml up -d
```

* Espera unos 15 segundos: al principio `app` aparece como `health: starting`
* Diagnostica el problema con `docker compose ps -a` y `docker compose logs app`
* Usa `config` con los mismos dos argumentos `-f` para encontrar la causa
* Recupera el servicio **sin borrar los datos**

¿Por qué reconstruir la imagen no arregla el problema?

**Comprueba el resultado:** Tras recuperar el servicio, la aplicación vuelve a estar saludable y muestra la tarea anterior.

**Limpieza y continuidad:** Una vez recuperado el servicio, ejecuta `docker compose down` desde la raíz para liberar 8080. Conserva el volumen; no uses `-v` hasta la limpieza final.

[Consultar solución](02-soluciones.md#práctica-20)

## Práctica 21

**Scout**

**Antes de empezar:** Copia local de `material/scout-demo` y Docker Scout disponible; no necesitas contenedores de otras prácticas.

* Construye la imagen `demo-service` a partir de `material/scout-demo`
* Analízala con `docker scout quickview`
* Modifica el `Dockerfile` aplicando la recomendación de imagen base (versión LTS de Node.js)
* Construye la Imagen Docker de nuevo
* Compara los resultados; actualizar no garantiza cero vulnerabilidades
* Extra: ¿qué vulnerabilidades altas quedan? ¿De dónde vienen?

**Comprueba el resultado:** Registra los resultados antes y después, con fecha, arquitectura y digest; explica el origen de las vulnerabilidades que quedan.

**Limpieza y continuidad:** No necesitas dejar contenedores en ejecución. Si editaste el Dockerfile, restaura `ARG NODE_VERSION=18` para conservar el punto de partida deliberadamente antiguo. Puedes guardar las imágenes para comparar los informes.

[Consultar solución](02-soluciones.md#práctica-21)

## Práctica 22

**Seguridad**

**Antes de empezar:** Copia local de `material/security-lab` y puerto 8080 libre. Detén el proyecto de la práctica 20 si sigue en ejecución.

Sigue el [laboratorio de seguridad](../material/security-lab/README.md) para
construir y probar la imagen inicial y observar la inyección de comandos.

* Escribe `material/security-lab/Dockerfile-2` a partir de `Dockerfile-1`
  * El contenedor se ejecuta con un usuario sin privilegios
  * No hay `bash` con *setuid* ni herramientas de red adicionales
* Construye la imagen `security-lab-2`
* Ejecútala limitando CPU a `0.5` y memoria a `256m`
* Repite el ataque: ¿qué usuario aparece ahora?
* Compara las dos imágenes con `docker scout quickview`

**Comprueba el resultado:** La aplicación sigue respondiendo y el ataque muestra un UID distinto de 0; explica si la inyección de comandos sigue siendo posible.

**Limpieza y continuidad:** Detén cada variante antes de arrancar la siguiente en 8080. Con los comandos del laboratorio, Ctrl+C termina y elimina el contenedor gracias a `--rm`. Si lo ejecutaste en segundo plano, elimina su contenedor con `docker rm -f <ID>`. Conserva tu Dockerfile-2.

[Consultar solución](02-soluciones.md#práctica-22)

## Práctica 23

**IA (opcional)**

**Antes de empezar:** Lee los requisitos en la guía de novedades. Si no puedes ejecutar Model Runner, realiza la alternativa de lectura; no necesitas recursos de otras prácticas.

Si tu equipo cumple los requisitos de Model Runner:

* Descarga `ai/smollm2:360M-Q4_K_M` y pregúntale "What is the difference between a Docker image and a container?"
* Compara la respuesta con lo aprendido. ¿Es correcta?
* Llama a la misma pregunta mediante la API con `curl`
* Libera la memoria con `docker model unload`

Si no:

* Lee `examples/ai/tutor.yaml` y explica qué pieza hace cada tarea: almacenar el modelo, generar texto, invocar una herramienta o aislar el entorno

> [Guía completa de novedades](04-novedades.md)

**Comprueba el resultado:** Contrasta la respuesta con la teoría o explica la función de cada componente en `examples/ai/tutor.yaml`.

**Limpieza y continuidad:** Si cargaste el modelo, libera su memoria con `docker model unload ai/smollm2:360M-Q4_K_M`. La alternativa de lectura no crea recursos.

[Consultar solución](02-soluciones.md#práctica-23)

## Limpieza final

Desde la raíz del repositorio, `docker compose down` permite hacer una pausa
sin borrar datos. Cuando hayas terminado y quieras borrar los datos de los
ejercicios:

```sh
docker compose down -v
docker volume rm training-sqlite training-mysql
```

Si omitiste una práctica, alguno de esos volúmenes puede no existir. Las demás
limpiezas están en cada enunciado. No uses `docker system prune` en un equipo
compartido. Conserva los Dockerfiles que hayas completado como trabajo realizado.
