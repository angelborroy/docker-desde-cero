# Funcionalidades adicionales: para qué sirven y cómo probarlas

[Índice](../README.md) | [Novedades e IA](04-novedades.md)

Los comandos parten de la raíz. Los ejemplos de Compose reutilizan el proyecto
principal salvo secrets y WordPress, que tienen proyectos y volúmenes independientes.

## BuildKit, Buildx y multi-stage

BuildKit ejecuta las construcciones; Buildx es el plugin CLI para acceder a sus
capacidades. Multi-stage permite copiar solo artefactos seleccionados de una
etapa a otra. No reduce automáticamente cualquier imagen: compara el resultado.

```sh
docker buildx version
docker build -f examples/Dockerfile.multistage -t training-tasks:multistage ./app
docker image ls training-tasks
docker run --rm --name training-multistage -p 127.0.0.1:8082:3000 training-tasks:multistage
```

Abre http://localhost:8082 y termina con Ctrl+C. La etapa de dependencias utiliza
un caché mount para descargas de npm. Esa caché no forma parte de la imagen final.

## Arquitecturas e imágenes multiplataforma

amd64 corresponde normalmente a Intel/AMD y arm64 a Apple Silicon y otros equipos
ARM. Una etiqueta puede apuntar a un índice con varias variantes.

```sh
docker buildx imagetools inspect node:24.22.0-trixie-slim
docker buildx imagetools inspect mysql:9.7.2
```

Busca `linux/amd64` y `linux/arm64`. Disponibilidad de una variante no equivale
a haber probado nuestra aplicación en ella. La emulación puede ser más lenta.
Publicar una imagen multiplataforma requeriría un registro y un builder adecuado;
no se necesita para seguir este curso.

## Compose Watch

Problema: reconstruir manualmente en cada cambio del código ralentiza el trabajo.
Este override sincroniza `src` y reinicia el proceso; si cambian los manifiestos,
reconstruye la imagen. Necesita Compose 2.23 o posterior.

```sh
docker compose -f compose.yaml -f examples/compose.watch.yaml up --watch
```

Edita el encabezado de `app/src/static/index.html`, guarda y recarga el navegador.
Resultado: se ve el cambio sin ejecutar `docker build` manualmente. Restaura el
texto original. Ctrl+C detiene el conjunto; recupera el recorrido normal con:

```sh
docker compose up -d --build --wait
```

Fuente: [Compose Watch](https://docs.docker.com/compose/how-tos/file-watch/).

## Perfiles y archivos adicionales

Un perfil activa servicios opcionales; varios archivos permiten superponer
configuración. No son conceptos intercambiables. Este servicio de diagnóstico
solo resuelve `db` desde la red del proyecto:

```sh
docker compose up -d --wait
docker compose -f compose.yaml -f examples/compose.profile.yaml --profile tools run --rm diagnostics
```

Resultado: `db =` seguido de una IP interna, que puede cambiar. El servicio
principal sigue funcionando al terminar. `run --rm` elimina el contenedor auxiliar.

## Secrets: archivos en vez de variables

El ejemplo independiente usa la misma contraseña pública del laboratorio en un
archivo. La monta en `/run/secrets/db_password`; la aplicación y MySQL la leen con
sus opciones `_FILE`. No es una credencial real ni un gestor de secretos cifrados.

```sh
docker compose -f examples/compose.secrets.yaml up -d --build --wait
```

Abre http://localhost:8081. Aquí los datos son independientes del proyecto principal.
La aplicación debe funcionar sin `MYSQL_PASSWORD` en su entorno.

```sh
docker compose -f examples/compose.secrets.yaml exec app node -e "console.log(process.env.MYSQL_PASSWORD === undefined)"
docker compose -f examples/compose.secrets.yaml down -v
```

Resultado: `true`. La limpieza elimina solo los datos de este ejemplo.
En Compose local el archivo de origen sigue en tu equipo; no se cifra por
declararlo secret. Las claves reales no deben estar en Git ni en una imagen.
[Secrets de Compose](https://docs.docker.com/compose/how-tos/use-secrets/).

## Recursos, reinicio y salud

```sh
docker run -d --name training-limits --memory 256m --cpus 1 --restart on-failure:3 -p 127.0.0.1:8082:3000 training-tasks:workshop
docker stats --no-stream training-limits
docker inspect training-limits
docker rm -f training-limits
```

Los límites controlan recursos. Una política de reinicio reacciona a la salida
del proceso. Un healthcheck evalúa disponibilidad: marcar `unhealthy` no reinicia
por si solo un contenedor. `depends_on` no es un supervisor permanente.

## Scout y SBOM

Una SBOM enumera componentes; un informe de vulnerabilidades los cruza con datos
conocidos. Sus resultados cambian con el tiempo. Cero hallazgos no garantiza
ausencia de problemas, y un hallazgo requiere analizar alcance y mitigación.

Con Docker Scout instalado y los requisitos de autenticación que indique:

```sh
docker scout version
docker scout sbom training-tasks:workshop
docker scout cves training-tasks:workshop
```

No hay un número esperado de CVE. Compara dependencias, versión de base y fecha.
[Documentación de Scout](https://docs.docker.com/scout/).

## Rootless

`USER node` selecciona un usuario dentro del contenedor. Rootless permite ejecutar
el motor y contenedores sin privilegios root en el host, con requisitos y límites
propios. No se cambia el motor durante el seminario.
[Rootless](https://docs.docker.com/engine/security/rootless/).
