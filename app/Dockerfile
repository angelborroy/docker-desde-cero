# syntax=docker/dockerfile:1
FROM node:24.22.0-trixie-slim
WORKDIR /app
COPY package.json package-lock.json ./
RUN npm ci --omit=dev && npm cache clean --force
COPY --chown=node:node src ./src
RUN mkdir /data && chown node:node /data
ENV NODE_ENV=production SQLITE_DB_LOCATION=/data/todo.db
USER node
EXPOSE 3000
CMD ["node", "src/index.js"]
