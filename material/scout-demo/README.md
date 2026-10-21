# Docker Scout demo

## Goal

Learn to scan an image for known vulnerabilities with Docker Scout. This project is intentionally out of date: it uses an old Node base image and an old version of Express. Scout should report critical and high findings and recommend a newer base image.

## Build and scan

Run these commands from the repository root.

```
docker build -t demo-service material/scout-demo
docker scout quickview demo-service
docker scout cves --only-severity critical,high demo-service
docker scout recommendations demo-service
```

## Expected result

`quickview` shows vulnerabilities for the target and the base image, and suggests an updated base image. `recommendations` suggests moving from `node:18-alpine` to a current Node line.

## Exercise

Apply the recommendation: edit the Dockerfile and set `ARG NODE_VERSION=24`. Rebuild and scan again. The base-image critical and high findings should drop.

```
docker build -t demo-service material/scout-demo
docker scout cves --only-severity critical,high demo-service
```
