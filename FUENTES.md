# Fuentes y licencias

Revisión documental: 2026-10-19. Material docente en español; código fuente,
comentarios, identificadores, configuraciones y mensajes de aplicación en inglés.

## Código de la aplicación

Origen: [docker/getting-started-app](https://github.com/docker/getting-started-app).
Revisión de partida:
[`6b025fc53bc7b9bef435d6b09bcd1da5a871c9cc`](https://github.com/docker/getting-started-app/tree/6b025fc53bc7b9bef435d6b09bcd1da5a871c9cc).

El backend de `app/src` deriva de ese proyecto, de Docker y sus colaboradores.
Su [package.json original](https://github.com/docker/getting-started-app/blob/6b025fc53bc7b9bef435d6b09bcd1da5a871c9cc/package.json)
declara licencia MIT; esa revisión no incluye archivo LICENSE independiente.
Se conserva la declaración en el manifiesto y se registra aquí la procedencia.
Las dependencias conservan sus propias licencias, disponibles en sus paquetes.

Adaptaciones del curso:

- Frontend propio de un archivo, sin fuentes ni scripts descargados desde CDN.
- Actualización de dependencias con versiones exactas y lockfile renovado.
- Sustitución de nodemon por `node --watch` para desarrollo opcional.
- Lectura UTF-8 y eliminación del salto final en configuraciones `_FILE` de MySQL.
- Dockerfile no root basado en Debian Trixie para compatibilidad con sqlite3 6
  en ARM; configuraciones Compose y ejemplos adicionales propios.

No se presenta esta adaptación como un producto oficial de Docker.

## Ejercicios derivados del taller de DockerCon 2023

Origen: [mikesir87/dockercon23-workshop-materials](https://github.com/mikesir87/dockercon23-workshop-materials),
revisión [`c19e03e`](https://github.com/mikesir87/dockercon23-workshop-materials/tree/c19e03e37bda8f6e5dceb3f6a96feb54dddee951).
Copyright 2023 Michael Irwin. Licencia Apache 2.0: texto completo en
[LICENSES/Apache-2.0-dockercon23-workshop.txt](LICENSES/Apache-2.0-dockercon23-workshop.txt).

Carpetas derivadas en `material/`: `database-initialization`, `dev-express`,
`first-build`, `multi-stage-react-app`, `nonroot-node-app` y
`simple-python-webapp`. Las soluciones de `solutions/multi-stage-react-app`,
`solutions/nonroot-node-app` y `solutions/simple-python-webapp` completan esos
mismos ejercicios.

Cambios respecto al original, realizados para este curso:

- Ficheros modificados: todos los Dockerfile, `package.json`, `requirements.txt`,
  los SQL de `database-initialization`, el código de `src/` y las hojas de estilo,
  y el README de `multi-stage-react-app`. Se actualizan imágenes base y
  dependencias y se adaptan los enunciados `TODO`.
- Ficheros añadidos: los README de cada ejercicio, los `.dockerignore` y los
  `package-lock.json`.
- Ficheros eliminados: los `yarn.lock` y `multi-stage-react-app/.eslintrc.cjs`.
- Sin cambios: `first-build/src/whale-hello-there.gif`,
  `multi-stage-react-app/index.html` y sus SVG de `public/` y `src/assets/`.

## Referencias oficiales por bloque

- [Conceptos de Docker](https://docs.docker.com/get-started/docker-concepts/).
- [Buenas prácticas de construcción](https://docs.docker.com/build/building/best-practices/).
- [Construcciones multi-stage](https://docs.docker.com/build/building/multi-stage/).
- [Volúmenes](https://docs.docker.com/engine/storage/volumes/).
- [Redes bridge](https://docs.docker.com/engine/network/drivers/bridge/).
- [Compose Specification](https://docs.docker.com/reference/compose-file/).
- [Orden de inicio](https://docs.docker.com/compose/how-tos/startup-order/).
- [Compose Watch](https://docs.docker.com/compose/how-tos/file-watch/).
- [Perfiles](https://docs.docker.com/compose/how-tos/profiles/).
- [Secrets](https://docs.docker.com/compose/how-tos/use-secrets/).
- [Docker Scout](https://docs.docker.com/scout/).
- [Rootless](https://docs.docker.com/engine/security/rootless/).
- [Model Runner](https://docs.docker.com/ai/model-runner/).
- [CLI de modelos](https://docs.docker.com/reference/cli/docker/model/).
- [MCP Toolkit](https://docs.docker.com/ai/mcp-catalog-and-toolkit/get-started/).
- [MCP Gateway](https://docs.docker.com/ai/mcp-catalog-and-toolkit/mcp-gateway/).
- [Docker Agent](https://docs.docker.com/ai/docker-agent/).
- [Proveedores de modelos para agentes](https://docs.docker.com/ai/docker-agent/providers/overview/).
- [Docker Sandboxes](https://docs.docker.com/ai/sandboxes/).
- [Sandboxes locales](https://docs.docker.com/ai/sandboxes/get-started/).

Las páginas de novedades cambian con frecuencia. La fecha anterior indica cuándo
se contrastaron nombres y comandos.

## Fuentes utilizadas en la revisión del 19 de octubre de 2026

- [Publicación de puertos](https://docs.docker.com/engine/network/port-publishing/).
- [Dockerfile: instrucciones y metadatos](https://docs.docker.com/reference/dockerfile/).
- [Fusión de Compose](https://docs.docker.com/compose/how-tos/multiple-compose-files/merge/).
- [Modelos y variables en Compose](https://docs.docker.com/reference/compose-file/services/#models).
- [API de Model Runner](https://docs.docker.com/ai/model-runner/api-reference/).
- [nologin](https://man7.org/linux/man-pages/man8/nologin.8.html).
- [Versiones soportadas de Node.js](https://nodejs.org/en/about/previous-releases).
- [Etiquetas de imágenes oficiales](https://github.com/docker-library/official-images/tree/master/library).

Las dependencias de Scout y la RCE del laboratorio
son deliberadamente inseguras; no son ejemplos de producción.
