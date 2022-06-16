- [Install Postgres](https://hub.docker.com/_/postgres)
- [Python with Redis](https://realpython.com/python-redis/)

Creamos un contenedor con Postgres:
> docker run -d -p 5432:5432  -e POSTGRES_PASSWORD=mypassword --name some-postgres postgres