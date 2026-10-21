FROM node:24.22.0-alpine

# A non-root user is created for you.
RUN adduser -D -u 10000 app-user

# Switch to the non-root user for all following actions and at runtime
USER app-user

# Set the working directory (created and owned by app-user)
WORKDIR /usr/local/app

# Copy the dependency manifests, owned by the non-root user
COPY --chown=app-user package.json package-lock.json ./

# Install the exact dependencies from the lock file
RUN npm ci

# Copy the application source, owned by the non-root user
COPY --chown=app-user src ./src

# Expose the application port
EXPOSE 3000

CMD ["node", "src/index.js"]
