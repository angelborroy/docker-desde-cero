# Docker práctico: de cero a despliegue seguro

Material del curso: guías, prácticas, ejemplos, comandos y soluciones.
No necesitas programar la aplicación. Necesitas Docker funcionando, una terminal
y saber cambiar de carpeta y editar un archivo.

Puedes seguir el material por tu cuenta o utilizarlo para impartir formaciones.
Los bloques y las prácticas permiten adaptar el recorrido al nivel del grupo y
al tiempo disponible, sin un calendario fijo.

## Antes de empezar

1. Completa la [comprobación previa](docs/00-preparacion.md).
2. Sigue los enunciados de la [guía de prácticas](docs/01-practicas.md).
   Cada práctica incluye requisitos, comprobación del resultado y limpieza.
   Mantén el índice abierto: lee en GitHub y ejecuta los ejercicios en tu copia
   local del repositorio, con el editor y la terminal.
3. Consulta las [soluciones](docs/02-soluciones.md) para comprobar tus resultados.
   Ambas guías usan la misma numeración, del 1 al 23. Las prácticas marcadas
   "(opcional)" permiten ampliar el recorrido.

## Índice del contenido

1. Fundamentos: imagen, contenedor, registro y VM.
2. Ejecutar y diagnosticar contenedores.
3. Dockerfile, capas, caché y construcción de imágenes.
4. Persistencia y redes.
5. Compose y sus capacidades adicionales.
6. Buenas prácticas y seguridad.
7. **[Novedades: modelos, MCP, agentes y Sandboxes](docs/04-novedades.md).**

## Referencias de trabajo

- [Comandos y errores habituales](docs/03-consulta.md).
- [Funcionalidades adicionales con ejemplos](docs/05-ampliaciones.md).
- [Fuentes y licencias](FUENTES.md).

## Licencia

El material se publica con la [licencia Apache 2.0](LICENSE). El contenido de
terceros conserva sus derechos y licencias; consulta [NOTICE](NOTICE) y la
[procedencia de los ejercicios](FUENTES.md).

## Ver la aplicación completa

Desde la raíz de esta carpeta:

```sh
docker compose up -d --build --wait
```

Abre http://localhost:8080 y crea una tarea. Se guarda en MySQL.
La primera descarga y construcción necesitan Internet.

```sh
docker compose down
```

Conserva los datos. Para borrar también los datos **de este proyecto**:

```sh
docker compose down -v
```

Las contraseñas incluidas son públicas y exclusivamente didácticas.
No hay autenticación de usuarios: la aplicación es un laboratorio local.

## Estructura

```text
docs/                 Guías, prácticas, soluciones y novedades
material/             Punto de partida de las prácticas
solutions/            Soluciones de referencia de las prácticas
app/                  Aplicación de tareas y Dockerfile completo
examples/             Compose, multi-stage y configuración de agentes
secrets/              Secreto de ejemplo para Compose
compose.yaml          Solución de aplicación + MySQL
```

Todos los comandos del curso se ejecutan desde la raíz de esta carpeta, salvo
indicación expresa. No se necesita cuenta Docker para el recorrido principal,
salvo las restricciones que pueda aplicar el registro a las descargas de tu red.
