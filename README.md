# Django-Postgres-Gunicorn-Nginx-Templates
This is a template for an django application using docker + postgres + nginx. This templates requires the environment variables. 

# Environment Variables
This templates requires 3 files to be created inorder to work. These files are .end.dev, .env.prod, and .env.prod.db. These files set the needed variables needed in django.setting and docker-compose files (both dev and production files). **They belong in the same directory as the docker-compose files. **

Here is an examples of what you needs: 

Example .env.dev

```
DEBUG=1
SECRET_KEY='%h+%ki!54-bd3j5rh2lmf(-wpu*jo2d(_0dvyh+%cpbq!-^#gc'
DJANGO_ALLOWED_HOSTS=localhost 127.0.0.1 [::1]
SQL_ENGINE=django.db.backends.postgresql
SQL_DATABASE=postgres
SQL_USER=postgres
SQL_PASSWORD=postgres
SQL_HOST=db
SQL_PORT=5432
DATABASE=postgres
```

Example .env.prod
```
DEBUG=0
SECRET_KEY='%h+%ki!54-bd3j5rh2lmf(-wpu*jo2d(_0dvyh+%cpbq!-^#gc'
DJANGO_ALLOWED_HOSTS=localhost 127.0.0.1 [::1]
SQL_ENGINE=django.db.backends.postgresql
SQL_DATABASE=postgres
SQL_USER=postgres
SQL_PASSWORD=postgres
SQL_HOST=db
SQL_PORT=5432
DATABASE=postgres
```

Example .env.prod.db
```
POSTGRES_DB=postgres
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
```

# Build
To build and run the development docker files (use sudo if you do not have root access):
1. docker-compose build
2. docker-compose up

To run the the production docker-compose (use sudo if you do not have root access):
1. docker-compose -f docker-compose.prod.yml build
2. docker-compose -f docker-compose.prod.yml up

# To shutdown
1. Press CLRL-C
2. docker-compose down
