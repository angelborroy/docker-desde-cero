FROM node:24.22.0-alpine

# A non-root user is created for you.
RUN adduser -D -u 10000 app-user

# TODO - Switch to the "app-user" user for all following actions and at runtime

# TODO - Set the working directory to /usr/local/app
#        (create it after USER so it is owned by app-user)

# TODO - Copy package.json and package-lock.json into the working directory.
#        Set the owner to "app-user" using the --chown option.
#        https://docs.docker.com/reference/dockerfile/#copy

# TODO - Run "npm ci" to install the dependencies

# TODO - Copy the "src" directory into a "src" subdirectory of the working
#        directory (set the owner to "app-user" with --chown)

# TODO - Expose port 3000

CMD ["node", "src/index.js"]
