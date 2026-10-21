# This image is intentionally out of date. We use an old Node base and an old
# version of Express so that "docker scout" reports vulnerabilities and suggests
# a newer base image. Do not copy this file as a good example.

# TODO (exercise) - After reading the Scout report, change this value to 24 and
# rebuild. The critical and high findings from the base image should drop.
ARG NODE_VERSION=18

FROM node:${NODE_VERSION}-alpine

ENV NODE_ENV=production
WORKDIR /usr/src/app

# Install the exact dependencies from the lock file
COPY package.json package-lock.json ./
RUN npm ci --omit=dev

# Run as the built-in non-root "node" user
USER node

# Copy the rest of the source
COPY . .

EXPOSE 3000
CMD ["npm", "start"]
