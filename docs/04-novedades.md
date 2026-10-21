# 7. Novedades de Docker: modelos, herramientas y agentes

[Índice](../README.md)

Revisión documental: 19 de octubre de 2026. Este bloque explora modelos,
herramientas y agentes en el ecosistema Docker. Es una sección independiente:
no necesitas ejecutar estos ejemplos para completar las prácticas fundamentales.

## El mapa: cinco piezas diferentes

| Pieza | Qué problema resuelve | No confundir con |
|---|---|---|
| Modelos como artefactos OCI | Distribuir pesos y metadatos mediante registros. | Un contenedor con un servidor arrancado. |
| Model Runner | Cargar modelos y ejecutar inferencia. | El agente que decide que herramientas utilizar. |
| MCP Catalog / Toolkit / Gateway | Descubrir, gestionar y conectar herramientas. | El modelo que genera las respuestas. |
| Docker Agent | Definir agentes, instrucciones, modelos y delegación. | Gordon, el asistente integrado de Docker. |
| Docker Sandboxes | Aislar un entorno de trabajo para agentes de programación. | La ejecución de un modelo de IA. |

Un agente puede usar un modelo servido por Model Runner y herramientas expuestas
por MCP. Un sandbox limita el entorno en el que trabaja un agente. Son capacidades
complementarias; no hace falta activar todas para demostrar una de ellas.

## 7.1 Modelos en Docker Hub y OCI

OCI permite distribuir otros artefactos además de imágenes de contenedor.
Un modelo empaquetado contiene pesos y metadatos; no es una imagen que se arranque
con `docker run`. Usa `docker model` para las operaciones del modelo.
Revisa publicador, licencia y requisitos en su ficha; estar en un registro no
implica que cualquier artefacto sea confiable o haya sido verificado.

```sh
docker model --help
docker model pull ai/smollm2:360M-Q4_K_M
docker model inspect ai/smollm2:360M-Q4_K_M
docker model list
```

Resultado esperado: el modelo aparece en el inventario de Model Runner.
La descarga requiere Internet y espacio adicional. El alias puede cambiar;
registra el identificador que devuelve `inspect` para repetir una demostración.

Fuente: [referencia de docker model](https://docs.docker.com/reference/cli/docker/model/).

## 7.2 Docker Model Runner: demostración mínima

Antes: habilita Model Runner en una instalación compatible y comprueba sus
[requisitos por plataforma](https://docs.docker.com/ai/model-runner/).
macOS utiliza Apple Silicon; las opciones de GPU en Windows y los backends de
Linux dependen del equipo y del motor de inferencia. No se exige GPU al curso.
No supongas que un modelo que cabe en disco también cabe en memoria.

```sh
docker model status
docker model run ai/smollm2:360M-Q4_K_M "Explain the difference between a Docker image and a container in three sentences."
```

Resultado esperado: texto generado. La respuesta varía y puede ser incorrecta;
contrasta la definición con lo aprendido. No es un test con una salida literal.
Tras la demostración, descarga el modelo de memoria:

```sh
docker model unload ai/smollm2:360M-Q4_K_M
```

Si no quieres conservar sus archivos:

```sh
docker model rm ai/smollm2:360M-Q4_K_M
```

DMR ofrece API de inferencia, además de CLI. En Linux sus motores se ejecutan
en contenedores; en macOS y Windows se ejecutan en el host, dentro de un sandbox
del sistema operativo, no en un contenedor.
[Arquitectura y plataformas](https://docs.docker.com/ai/model-runner/).

### API desde el host y desde contenedores

Con acceso TCP activado en Desktop (puerto 12434), desde la raíz del curso:

```sh
curl http://localhost:12434/engines/v1/chat/completions -H "Content-Type: application/json" --data-binary @examples/ai/chat-request.json
```

En Windows PowerShell usa `curl.exe` y pasa el archivo como
`--data-binary "@examples/ai/chat-request.json"`. El archivo evita los problemas de
comillas del JSON entre shells. El modelo debe estar descargado.

Desde un contenedor en Desktop, la URL base es
`http://model-runner.docker.internal/engines/v1`. En Docker Engine, declara
`extra_hosts: ["model-runner.docker.internal:host-gateway"]` y usa el puerto 12434:
`http://model-runner.docker.internal:12434/engines/v1`. Verifica que el endpoint
esté accesible desde esa red. La API no tiene autenticación incorporada; limita
su acceso y no la publiques en una red no confiable.

La compatibilidad cubre endpoints concretos, como chat completions y embeddings;
no implica que todas las funciones de cualquier SDK estén disponibles.
[Referencia de la API](https://docs.docker.com/ai/model-runner/api-reference/).

### Modelos en Compose

Requiere Compose 2.38 o posterior y Model Runner. En la sintaxis larga declara
`endpoint_var: LLM_URL` y `model_var: LLM_MODEL` para fijar los nombres que lee la
aplicación. La sintaxis corta también genera dos variables a partir de la clave:
en mayúsculas, `-` pasa a `_`, y se añade `_URL` y `_MODEL` (la clave `llm` da
`LLM_URL` y `LLM_MODEL`). Compose descarga el modelo y configura las variables. [Referencia de models](https://docs.docker.com/reference/compose-file/services/#models).

## 7.3 MCP: catálogo, gestión y conexión

MCP proporciona un protocolo para que un cliente descubra e invoque herramientas.
El **Catalog** ayuda a encontrarlas, **Toolkit** organiza servidores y clientes,
y **Gateway** intermedia las conexiones y la ejecución de los servidores.

Ejemplo: un asistente consulta una página mediante un servidor de herramientas.
La capacidad de acceder a la página pertenece a la herramienta, no a los pesos
del modelo. Cada servidor conserva sus propios permisos y requisitos.

Con Docker Desktop compatible, habilita MCP Toolkit y crea un perfil exclusivo
del curso. Añade un servidor de lectura desde Catalog y conecta tu cliente desde
Clients. Comprueba que el cliente lista sus herramientas y pide una consulta de
lectura. El resultado debe mostrar la llamada a la herramienta, no solo una
respuesta del modelo. Al terminar, desconecta el cliente y elimina el perfil
del curso desde Toolkit, sin modificar tus perfiles habituales.

La interfaz con perfiles corresponde a Docker Desktop 4.62 o posterior.
Toolkit figura como Beta en la referencia consultada.
[Recorrido oficial](https://docs.docker.com/ai/mcp-catalog-and-toolkit/get-started/).

Para comprender el proceso sin modificar tus perfiles, este comando inicia un
gateway con un servidor explícito del catálogo. Necesita Docker MCP instalado,
acceso al catálogo y la imagen del servidor:

```sh
docker mcp gateway run --servers fetch
```

Usa stdio: no abre una página en el navegador y queda esperando un cliente MCP.
Termina con Ctrl+C. La disponibilidad del servidor depende del catálogo actual.
En un cliente que acepte `mcpServers`, la configuración equivalente es:

```json
{
  "mcpServers": {
    "training-docker": {
      "command": "docker",
      "args": ["mcp", "gateway", "run", "--servers", "fetch"]
    }
  }
}
```

El nombre del campo exterior depende del cliente; no reemplaces su archivo
completo con este fragmento. Limita la demostración a leer una página pública.
[Gateway y opciones de instalación](https://docs.docker.com/ai/mcp-catalog-and-toolkit/mcp-gateway/).

## 7.4 Docker Agent: la evolución de cagent

El nombre actual es **Docker Agent** y el comando es `docker agent`.
Docker Desktop 4.49-4.62 utilizaba el nombre cagent; desde 4.63 se incluye con el
nombre actual. También hay instalación independiente.
[Referencia oficial](https://docs.docker.com/ai/docker-agent/).

El ejemplo [tutor.yaml](../examples/ai/tutor.yaml) contiene un coordinador y un
especialista en persistencia y redes. Ambos usan un modelo local y no tienen
herramientas de shell ni de sistema de archivos. Las instrucciones del código
están en inglés y piden responder en español.

Este ejemplo es más exigente que `smollm2`: necesita un modelo capaz de manejar
delegación y suficiente memoria. Consulta primero la ficha de `ai/qwen3` y no
lo descargues si no cumple las capacidades de tu equipo.

```sh
docker agent version
docker model pull ai/qwen3
docker agent run examples/ai/tutor.yaml
```

Pregunta sugerida: "Why did my task disappear after removing the container?"
Observa si se produce la delegación, y evalúa la explicación. La ejecución y el
tool calling dependen del modelo; no se promete una respuesta determinista.
Sal con Ctrl+C. Puedes conservar el modelo o liberar memoria con
`docker model unload ai/qwen3`; `docker model rm ai/qwen3` elimina sus archivos.

Gordon (`docker ai`) es el asistente de Docker. Requiere Docker Desktop 4.74 o
posterior y haber iniciado sesión. Docker Agent es el framework
para definir tus propios agentes. Un agente tampoco sustituye las comprobaciones
de `logs`, `inspect` y `config`.
[Proveedores y ejecución local](https://docs.docker.com/ai/docker-agent/providers/overview/).

## 7.5 Docker Sandboxes: entorno para agentes de programación

La documentación actual usa **`sbx`**, instalado por separado. No copies sin revisar
los ejemplos antiguos de `docker sandbox`. Los sandboxes locales utilizan microVM
y disponen de su propio entorno; la carpeta compartida sigue siendo accesible
al agente. También existe ejecución cloud, fuera del alcance de este curso.
[Descripción actual](https://docs.docker.com/ai/sandboxes/).

Demostración opcional: instala `sbx`, inicia sesión en Docker y configura la
autenticación del agente siguiendo la documentación. Puede requerir suscripción
o credenciales del proveedor. Usa una carpeta vacía de demostración:

```sh
mkdir training-sandbox-demo
cd training-sandbox-demo
sbx run --name training-demo claude
```

Solicita: "Create a hello.txt file containing Hello from the sandbox."
Comprueba el archivo en la carpeta compartida. En otra terminal:

```sh
sbx ls
sbx stop training-demo
sbx rm training-demo
```

Eliminar el sandbox no deshace los cambios en la carpeta compartida. Revisa y
elimina el archivo de demostración con tu editor si ya no lo necesitas.
La primera ejecución puede pedir configurar la política de red global: revisa
su alcance antes de cambiarla. [Guía local y limpieza](https://docs.docker.com/ai/sandboxes/get-started/).

## Si no puedes ejecutar IA en tu equipo

Sigue los ejemplos y lee las configuraciones. Explica qué pieza realiza cada
tarea: almacenar un modelo, generar texto, invocar una herramienta o aislar un
entorno. Esta distinción es el objetivo del bloque; disponer de hardware para
inferencia no es un requisito del seminario.
