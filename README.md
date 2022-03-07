# intros-ai

## Runinng the application

The best way to review the work so that it's easy to understand is to follow the commit history as I made sure to built it accordingly.

### Docker Compose

Included a `docker-compose.yml` file that can be used to build and spin up the three docker containers needed for the app:

- server: This is the backend tornado server container.
- mysql: The MySQL database service.
- app: The Typescript React web app.

If you don't have Docker and Docker Compose and want to use it to run this app, you can install it by following the instructions [here](https://docs.docker.com/compose/install/).

Once Docker Compose and Docker are installed you can run:

```
docker-compose build
```

to build the backend and frontend images, and then:

```
docker-compose up --remove-orphans
```

to run the containers.

IMPORTANT: The web app container binds the host port `80` and the MySQL service to the host port `3306` so if you have a webserver and/or a MySQL running on localhost, you'd need to stop them.

Once the containers are running use a MySQL client to connect to the DB on localhost using the user and password in the `docker-compose.yml` file, then execute the `sql/mindump.sql` script to create the database and table needed. You need to do this only the first time (given you don't delete the docker container volume).

Once the containers are running, you can go to `localhost` on your browser. Note that it takes a few seconds for the MySQL service to be reachable by the backend server, so if you can't reach it, try again in 10 to 20 seconds.

### Running the services

- Assuming you have a MySQL server running, execute the `sql/mindump.sql` script to create the database and table needed for the app.
- Create environment variables to configure your MySQL server connection info (DB_HOST, DB_PORT, DB_USER, DB_PASSWORD, DB_DATABASE).
- In a shell terminal, go into the `server/` directory, install the requirement using the command `pip3 install -r requirements.txt` and then run the python server with the command `python3 server.py`.
- In another shell terminal, go into the `app/` directory, install the frontend packages with `npm install` and then run the app with `npm start`. The app should be available at `http://localhost:3000` at this point.

## Considerations

For the backend server, this is completely a development server that shouldn't run in production. The main reason for this are the fact that we run the `server.py` directly and aren't using a webserver (e.g. NginX or Gunicorn) to do that.

Given more time, I'd do the following improvements:

- Refactor the frontend app by putting the base url and button style in a config file to use that across the app.
- Manage the React app state better to not have to refresh the page after each action.
- For the task creation, change it so that we don't use the form and submit type button but use simply an action button like the other buttons.
- Improve error handling both on the backend and frontend.
- Add the date components, both in the frontend and backend, so that each entry shows a date when it was added to the list, and a date at which it was last edited. I completely missed this part until the end.
