# Database initialization

## Goal

See how the official MySQL image runs SQL scripts on first start. Any `.sql` file placed in `/docker-entrypoint-initdb.d` runs in alphabetical order when the data directory is empty. Here `1-create-schema.sql` creates the table and `2-data.sql` inserts rows.

## Run

Run this command from the repository root. It mounts the scripts into the init folder.

```
docker run --rm --name db-init \
  -e MYSQL_ROOT_PASSWORD=classroom-only \
  -e MYSQL_DATABASE=workshop \
  -v ./material/database-initialization:/docker-entrypoint-initdb.d \
  mysql:9.7.2
```

Wait until the log shows `ready for connections`. Then, in another terminal, query the data:

```
docker exec db-init mysql -uroot -pclassroom-only -e "SELECT * FROM workshop.users;"
```

## Expected result

You see the two rows: `Moby Dock` and `Whale Watcher`.

Press Ctrl+C in the first terminal to stop the container.
