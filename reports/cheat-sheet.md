# Cheat sheets and checklists

- Student name: Xander Van der Linden
- GitHub repo: <https://github.com/HOGENT-MLOps/mlops-2425-xvanderlinden>

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

## Labo 2 CI/CD

| Task                          | Command                                                     |
| :-----------------------------| :---------------------------------------------------------- |
| Set global username            | `git config --global user.name "Your Name"`                 |
| Set global email               | `git config --global user.email "Your@Name.com"`            |
| Check Git configuration        | `git config --global --list`                               |
| Initialize a Git repository     | `git init`                                                 |
| Add all files to staging        | `git add .`                                                |
| Commit with a message           | `git commit -m "Your commit message"`                      |
| Push to the main branch         | `git push origin main`                                     |
| Clone a repository              | `git clone <repository-url>`                               |
| Set remote origin               | `git remote add origin <repository-url>`                   |
| Install project dependencies    | `yarn install`                                             |
| Run linter                      | `yarn lint`                                                |
| Run tests                       | `yarn test`                                                |
| Create a Docker image           | `docker build -t <image-name> .`                           |
| Run a Docker container          | `docker run -p 3000:3000 <image-name>`                     |
| Push Docker image to Docker Hub | `docker push <dockerhub-username>/<image-name>`            |
| Pull Docker image from Docker Hub| `docker pull <dockerhub-username>/<image-name>`           |

## Labo 3 - MLFlow Cheatsheet

| Taak                                         | Commando                                                    |
| :------------------------------------------ | :---------------------------------------------------------- |
| Gebruik Python's ingebouwde `venv` module om een virtuele omgeving aan te maken | `python3 -m venv venv`                                      |
| Activeer de virtuele omgeving (Windows)     | `.\venv\Scripts\Activate`                                  |
| Controleer het pad naar Python              | `Get-Command python`                                         |
| Controleer het pad naar pip                 | `Get-Command pip`                                            |
| Start de Prefect server (Linux/macOS)       | `export PREFECT_HOME=$(pwd)/prefect_home`                   |
| Start de Prefect server (Windows)           | `$Env:PREFECT_HOME = "$(Get-Location)/prefect_home"`         |
| Start de Prefect server                     | `prefect server start`                                      |
| Start de MLFlow server                      | `mlflow server`                                             |
| Zet MLFlow system metrics logging op true   | `export MLFLOW_ENABLE_SYSTEM_METRICS_LOGGING=true`           |
| Start MLFlow met logging                    | `python -m mlflow.server`                                   |
| Log een MLFlow experiment                   | `mlflow.start_run()`                                         |
| Log metrics met MLFlow                      | `mlflow.log_metric("metric_name", value)`                    |
| Log een model met MLFlow                    | `mlflow.log_artifact("pad_naar_model")`                      |
| Zet de MLFlow tracking URI                  | `mlflow.set_tracking_uri("http://localhost:5000")`           |

## Labo 4 - Kubernetes

| Taak                                         | Commando                                                    |
| Real time (zo goed als) service opvragen     | `while (1) { kubectl get all; sleep 1 } `                   |
kubectl get deployments
kubectl get all  
kubectl get nodes
kubectl get pods
kubectl config view
kubectl create deployment hello-node --image=registry.k8s.io/e2e-test-images/agnhost:2.39 -- /agnhost netexec --http-port=8080
kubectl expose deployment hello-node --type=LoadBalancer --port=8080
kubectl get services
minikube service hello-node x 
minikube start
minikube dashboard
kubectl logs hello-node-66d457cb86-k45gr
kubectl apply -f echo-deployment.yml
kubectl apply -f echo-service.yml
minikube service echo-service x 
kubectl apply -f echo-all.yml
minikube service echo-all-service x
kubectl apply -f echo-all.yml ( ook voor changes)
kubectl get pods -o wide ( zien bij welke node elke pod hoort)
for ($i = 1; $i -le 10; $i++) { curl http://127.0.0.1:59623/ } 3 keer andere urls 
for ($i = 1; $i -le 10; $i++) { curl http://127.0.0.1:59623/ }
for ($i = 1; $i -le 10; $i++) { curl http://127.0.0.1:59623/ }
kubectl logs hello-node-66d457cb86-k45gr  


kubectl label pod echo-all-deployment-78cdcd9dbf-nm4b5  application_type=demo
error: 'application_type' already has a value (demo), and --overwrite is false <errormessage zonder --overwrite>
kubectl label pod echo-all-deployment-78cdcd9dbf-nm4b5  application_type=production --overwrite