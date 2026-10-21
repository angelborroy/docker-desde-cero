# Comandos y errores habituales

[Índice](../README.md)

## Comandos copiables

Estado y diagnóstico del proyecto:

```sh
docker version
docker context show
docker context ls
docker compose ps -a
docker compose logs --tail 50 app
docker compose config
docker compose exec app id
docker compose exec app node -e "require('dns').lookup('db', console.log)"
docker compose exec app node -e "fetch('http://localhost:3000/items').then(r=>r.json()).then(console.log)"
```

`context` selecciona a que motor hablas. No cambies a un contexto remoto para
seguir un ejercicio local sin comprobar antes dónde se crearán sus recursos.

Cambios y limpieza:

```sh
docker compose up -d --build --wait
docker compose stop
docker compose start
docker compose down
```

`down` elimina contenedores y red del proyecto; no sus volúmenes nombrados.
`down -v` elimina también esos volúmenes y sus datos.

## Cuando algo falla

| Síntoma | Comprobación y solución |
|---|---|
| No conecta al daemon | Inicia Docker Desktop; revisa `docker context show` y Client/Server en `docker version`. |
| Puerto ocupado | Comprueba `docker ps`. En Compose cambia `APP_PORT` en `.env`; en `run`, cambia el puerto izquierdo de `-p`. |
| Nombre en uso | Busca con `docker ps -a`. Arranca el existente o elimina solo el contenedor del ejercicio. |
| No resuelve `db` | Usa la misma red; revisa `MYSQL_HOST`. El DNS de Compose no es el DNS del equipo. |
| MySQL no acepta conexiones | Espera al healthcheck y consulta `docker compose logs db`. El proceso iniciado no implica servicio disponible. |
| Access denied tras cambiar password | El volumen conserva los usuarios anteriores. Restaura la credencial o cambia el usuario mediante SQL; no borres datos para ocultar el problema. |
| Desaparecen tareas al cambiar a MySQL | Es otra base de datos. Este curso no realiza migración desde SQLite. |
| El navegador sigue mostrando lo anterior | Recrea el contenedor con la imagen nueva y recarga la página. |
| Error de permisos con un bind mount | Revisa usuario y permisos de la carpeta del equipo. Evita resolverlo ejecutando todo como root. |
| Image not found o límite de descargas | Revisa etiqueta, conexión y respuesta del registro. Descarga antes de clase. |
| No matching manifest | Comprueba arquitectura y etiqueta. No fuerces amd64 en ARM como primera solución. |
| Modelo IA no arranca | Revisa requisitos de Model Runner; no es un problema del laboratorio básico. |

## Rutas de bind mounts

En las prácticas se prefieren volúmenes y rutas relativas en Compose.
Para un bind mount manual de código, usa la variante de tu terminal.
Primero construye `training-tasks:workshop`. Usa el puerto 8082 para no colisionar.

Bash/Zsh, desde la raíz:

```sh
docker run --rm --name training-bind -p 127.0.0.1:8082:3000 --mount "type=bind,source=$(pwd)/app/src/static,target=/app/src/static,readonly" training-tasks:workshop
```

PowerShell, desde la raíz:

```powershell
docker run --rm --name training-bind -p 127.0.0.1:8082:3000 --mount "type=bind,source=$($PWD.Path)/app/src/static,target=/app/src/static,readonly" training-tasks:workshop
```

Abre http://localhost:8082 y edita el HTML: recargar muestra el cambio sin construir.
Termina con Ctrl+C. El montaje es de solo lectura para el contenedor; el editor del
equipo puede seguir cambiando el archivo. No copies la variante Bash en PowerShell.
