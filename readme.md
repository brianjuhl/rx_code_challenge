# Overview
Code repository for Brian Juhl's solution to the RX Savings Solutions code challenge. Technologies used 
in this project include: 

- Python 3
- FastAPI
- MongoDB
- Docker

# Running Locally
First make sure [Docker and Docker Compose](https://docs.docker.com/get-docker/) are installed on your machine. 

Once Docker is configured, simply pull down the code, bash```cd``` into the project directory and run bash``` docker-compose up -d --build``` to build the docker images and start the containers in detached mode. 

<!-- docker exec -it rx_code_challenge_api green -vvv -r -->