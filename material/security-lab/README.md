# Security lab

## Goal

Study the security properties of an image. You get a Spring Boot app with an intentional remote code execution (RCE) bug in the `/math` endpoint. The provided `Dockerfile-1` is insecure on purpose: it runs as root, keeps a setuid `/bin/bash` and stores secret flag files. Your task is to write a hardened version, `Dockerfile-2`, that reduces privileges while keeping the app working. The RCE and demonstration
flags remain intentionally present in both variants; neither is a production image.

The build is multi-stage, so you do not need Java or Maven installed. The first stage compiles the app with Maven.

## Build and run the insecure image

Run these commands from the repository root.

```
docker build -t security-lab-1 -f material/security-lab/Dockerfile-1 material/security-lab
docker run --rm -p 127.0.0.1:8080:8080 security-lab-1
```

Confirm the app answers:

```
curl "http://localhost:8080/math?factorize=12"
```

You get the prime factors of 12.

The endpoint is vulnerable to command injection. Confirm it by passing shell input (URL-encoded `1'; id #`):

```
curl "http://localhost:8080/math?factorize=1%27%3B%20id%20%23"
```

The output includes the result of `id`, which runs as root.

## Your task

Write `material/security-lab/Dockerfile-2`. Keep the app working but:

1. Run the container as a non-root user.
2. Do not add a setuid shell or extra network tools.
3. Limit resources at run time, for example `--cpus=0.5 --memory=256m`.

Then build and run it:

```
docker build -t security-lab-2 -f material/security-lab/Dockerfile-2 material/security-lab
docker run --rm --cpus=0.5 --memory=256m -p 127.0.0.1:8080:8080 security-lab-2
```

Check the user is no longer root:

```
docker run --rm --entrypoint id security-lab-2
```

Stop the first container before starting the second: they use the same port.
Do not reuse this intentionally vulnerable application outside the local exercise.

## Expected result

The hardened container runs as uid 10001, not root. The app still answers on `/math`. A reference solution is in `solutions/security-lab/Dockerfile`.
