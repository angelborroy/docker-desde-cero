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

# TODO - Add a second stage based on nginx:1.30.6-alpine that copies the built
#        assets from the "build" stage (/usr/local/app/dist) into
#        /usr/share/nginx/html. nginx already listens on port 80.
