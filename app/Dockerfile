FROM python:3.7-alpine
MAINTAINER SimpleGuide

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install psycopg2 dependencies
RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt /requirements.txt

# install Pillow & dependencies
RUN apk add --no-cache jpeg-dev zlib-dev
RUN apk add --no-cache --virtual build-deps build-base linux-headers

RUN pip install -r /requirements.txt

# copy project
RUN mkdir /app
WORKDIR /app
ADD . /app/

# copy entrypoint.sh
COPY ./entrypoint.sh /app/

RUN mkdir -p /media_cdn
RUN mkdir -p /static_cdn

# run entrypoint.sh
ENTRYPOINT ["/app/entrypoint.sh"]