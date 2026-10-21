# Multi-stage React app

## Goal

Build a Vite + React app with a multi-stage Dockerfile. The first stage (the `build` stage) is given. You write the second stage: start from `nginx:1.30.6-alpine` and copy the built assets from the `build` stage into `/usr/share/nginx/html`.

## Build and run

Run these commands from the repository root.

```
docker build -t multi-stage-react-app material/multi-stage-react-app
docker run --rm -p 127.0.0.1:8080:80 multi-stage-react-app
```

## Expected result

Open http://localhost:8080 in a browser. You see the Vite + React starter page. The final image is small because it only contains nginx and the static files, not Node or the build tools.

A full working Dockerfile is in `solutions/multi-stage-react-app/Dockerfile`.
