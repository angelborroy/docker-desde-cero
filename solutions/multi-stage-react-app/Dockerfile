FROM node:24.22.0-alpine AS build
WORKDIR /usr/local/app

# Install the build dependencies from the lock file
COPY package.json package-lock.json ./
RUN npm ci

# Copy the rest of the config and the application source
COPY vite.config.js index.html ./
COPY public ./public
COPY src ./src

# Build the static assets into /usr/local/app/dist
RUN npm run build

# Second stage: serve the built assets with nginx
FROM nginx:1.30.6-alpine
COPY --from=build /usr/local/app/dist /usr/share/nginx/html
