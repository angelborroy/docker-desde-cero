# Non-root Node app

## Goal

Complete the Dockerfile for a small Express API. A non-root user `app-user` is already created for you. You add the `WORKDIR`, the `COPY --chown` lines, the `USER` instruction, `RUN npm ci`, the source copy and `EXPOSE 3000`. The container must run as the non-root user.

## Build and run

Run these commands from the repository root.

```
docker build -t nonroot-node-app material/nonroot-node-app
docker run --rm -p 127.0.0.1:3000:3000 nonroot-node-app
```

## Expected result

Call the endpoint:

```
curl http://localhost:3000/api/message
```

You get `{"message":"Hello world!"}`.

Check the container runs as the non-root user (uid 10000):

```
docker run --rm nonroot-node-app id
```

A full working Dockerfile is in `solutions/nonroot-node-app/Dockerfile`.
