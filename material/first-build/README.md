# First build

## Goal

Build your first Docker image and run it. The image serves a small static web page with nginx.

## Build and run

Run these commands from the repository root.

```
docker build -t first-build material/first-build
docker run --rm -p 127.0.0.1:8080:80 first-build
```

## Expected result

Open http://localhost:8080 in a browser. You see a page with the heading "Congrats!" and a whale animation.

Press Ctrl+C to stop the container.
