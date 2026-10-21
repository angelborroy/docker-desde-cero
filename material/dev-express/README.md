# Dev container with live reload

## Goal

Run an application inside a container using a bind mount, so changes you make on the host reload automatically. No image build is needed. The app uses only the Node.js standard library, so it works even when there is no `node_modules` folder on the host. The `npm run dev` script uses `node --watch` to restart on every file change.

## Run

Run this command from the repository root.

```
docker run -it --rm -v ./material/dev-express:/app:ro --user node -w /app -p 127.0.0.1:3000:3000 node:24.22.0-alpine npm run dev
```

## Expected result

Call the endpoint:

```
curl http://localhost:3000/api/message
```

You get `{"message":"Hello Cats!"}`.

Now edit `material/dev-express/src/index.js` on the host and change the message text. Save the file. The server restarts automatically. Call the endpoint again and you see the new message.

Press Ctrl+C to stop the container.
