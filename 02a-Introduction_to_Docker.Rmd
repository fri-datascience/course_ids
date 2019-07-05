# Docker container platform

TODO: write about virtualization technologies, containers, ... Mention other virtualization technologis (VMWare, Virtualbox), containerized versions (Docker, Singularity) and something in between (Vagrant), ...

## Why Docker?

TODO: provide main docker features

## Setting up the environment

TODO: provide instructions to install and run docker
TODO: overview of accompanying apps (e.g. Kitematic)

## Short introduction to Docker

### Basics

TODO: run hello world container, get to know shell, logs, exec, ssh into container

### Understanding Docker ecosystem

TODO: overview

#### Images and containers

TODO: overview - difference, show based on the above example

#### Volumes

TODO: overview, why needed -example

#### Dockerfiles

TODO: overview
TODO: write a simple Python Flask service, write a Dockerfile script and run it

```
FROM ubuntu:18.04

WORKDIR /classroom
ADD ./ .


RUN apt-get update \
    && apt-get install -y wget \
    && wget https://repo.anaconda.com/archive/Anaconda3-2019.03-Linux-x86_64.sh \
    && bash Anaconda3-2019.03-Linux-x86_64.sh -b -p /anaconda3  \
    && /anaconda3/bin/conda install -y -c anaconda flask \

EXPOSE 8787

ENTRYPOINT /anaconda3/bin/python server.py
```

#### Docker compose

TODO: overview
TODO: upgrade the above example with database functionality:

A) First upgrade the app from before and use only the DB from DockerHub (explain volumes in pracice!)

```
FROM mysql:5 as database

ADD ./databaseScript/ /docker-entrypoint-initdb.d

RUN /bin/bash -c 'chmod a+rx /docker-entrypoint-initdb.d/*'
```

B) Write a docker compose script to run both containers simultaneously

```
version: '3.1'

services:

  database:
    image: database
    build: ./database
    command: --default-authentication-plugin=mysql_native_password
    restart: always
    environment:
      MYSQL_ROOT_PASSWORD: BeReSeMi.DataScience
    ports:
      - 3306:3306
    volumes:
      - ds_databases:/var/lib/mysql
    networks:
      - dsnet

  application:
    image: application
    build: ./application    
    depends_on:
      - database
    restart: always
    ports:
      - "8787:8787"
    networks:
      - dsnet

networks:
  dsnet:
    driver: bridge

volumes:
  ds_databases: 
```

#### Docker Hub

TODO: show how to publish your own images on the repo, how to search for them, ...

## Further reading and references

* Docker tutorial: https://docs.docker.com/get-started/
* Kubernetes, ...

## Learning outcomes

Data science students should work towards obtaining the knowledge and the skills that enable them to:

* Use an existing Docker image.
* Package a project into a Docker image and publish it on Docker Hub.


## Practice problems

* Create a simple Python program, write a Dockerfile to compile an image an publish it on Docker Hub.
* Write a service, which needs multiple servers deployed and run everything using docker compose.
