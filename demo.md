# Demo1 commando's

## 1. Show that you created a Docker image for the API
docker build xvanderlinden/webapp .

docker images 

## 2. Show that you can start the API using the SQLite database

docker-compose -d -f docker-compose-sqlite.yml up

curl http://localhost:3000/animals

## 3 Show that you can start the API using the MySQL database

docker-compose up -d (sql)

docker-compose logs webapp (sql database)

## 4. Show that you can access the API on port 3000

curl http://localhost:3000/animals/1

## 5 Show that you optimized the Docker image size

docker images (alpine en dockerignore)

## 6. Show all running containers in the Portainer dashboard

portainer(zie google)

## 7. Show that all tests are passing

docker-compose run test

docker image rm xvanderlinden/webapp
docker pull xvanderlinden/webapp

