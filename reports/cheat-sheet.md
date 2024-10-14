# Cheat sheets and checklists

- Student name: NAME
- GitHub repo: URL

## Basic commands

| Task              | Command           |
| :---------------- | :---------------- |
| Change directory  | `cd DIRECTORY`    |
| List files        | `ls -l`           |
| Create directory  | `mkdir DIRECTORY` |
| Create empty file | `touch FILE`      |
| Copy file         | `cp FILE DEST`    |
| Move file         | `mv FILE DEST`    |

## Docker commands

| Task                | Command                 |
| :------------------ | :---------------------- |
| List all containers | `docker ps -a`          |
| List all images     | `docker images`         |
| Stop a container    | `docker stop CONTAINER` |
| Remove a container  | `docker rm CONTAINER`   |

## Git workflow

Simple workflow for a personal project without other contributors:

| Task                                         | Command                   |
| :------------------------------------------- | :------------------------ |
| Current project status                       | `git status`              |
| Select files to be committed                 | `git add FILE...`         |
| Commit changes to local repository           | `git commit -m 'MESSAGE'` |
| Push local changes to remote repository      | `git push`                |
| Pull changes from remote repository to local | `git pull`                |

## Checklist network configuration

1. Is the IP address correct? `ip a`
2. Is the router/default gateway correct? `ip r -n`
3. Is a DNS-server available? `cat /etc/resolv.conf`

## Labo 1 Docker

| Task                     | Command                                                     |
| :------------------------| :---------------------------------------------------        |
| Change directory         | `cd .\resources\02-dockerlab\`                              |
| Start Portainer Container| `docker compose -f .\docker-compose.portainer.yml up -d`    |
| Build Docker Image       | `docker build -t webapp .`                                  |
| Run Docker Image         | `docker run -d -p 3000:3000 --name webapp_container webapp` |
| Fetch Animal Data (GET)  | `curl http://localhost:3000/animals`                        |
| Add Animal Data (POST)       | `curl -X POST -H "Content-Type: application/json" -d '{"name":"Lion","age":4}' http://localhost:3000/animals` |
| Remove Docker Container        | `docker rm webapp_container`                          |
| Start Webapp and Database     | `docker compose up -d`                                 |
| Stop Docker Container          | `docker stop webapp_container`                        |
| Update .gitignore             | `echo "dockerlab/webapp/database" >> .gitignore`       |
| Copy Docker Compose File      | `cp docker-compose.yml docker-compose-sqlite.yml`      |
| Run Tests                     | `docker compose run test`                              |
