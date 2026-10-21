// This app only uses the Node.js standard library, so it runs with a bind mount
// even when there is no node_modules folder on the host.
const http = require("node:http");

const server = http.createServer((request, response) => {
  if (request.url === "/api/message") {
    response.writeHead(200, { "Content-Type": "application/json" });
    response.end(JSON.stringify({ message: "Hello Cats!" }));
    return;
  }
  response.writeHead(404, { "Content-Type": "application/json" });
  response.end(JSON.stringify({ error: "Not found" }));
});

server.listen(3000, () => console.log("Listening on port 3000"));
