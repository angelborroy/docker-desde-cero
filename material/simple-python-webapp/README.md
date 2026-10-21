# Simple Python web app

## Goal

Complete the Dockerfile for a small Flask web app. The `FROM` and `WORKDIR` lines are given. You fill in the `# TODO -` lines to copy files, install dependencies and expose the port.

## Build and run

Run these commands from the repository root.

```
docker build -t simple-python-webapp material/simple-python-webapp
docker run --rm -p 127.0.0.1:5000:5000 simple-python-webapp
```

This introductory example uses Flask's development server. It is not a production
deployment template; production needs a WSGI server and a non-root runtime user.

## Expected result

Open http://localhost:5000 in a browser. You see a page with the title "Hello world!".

A full working Dockerfile is in `solutions/simple-python-webapp/Dockerfile`.
