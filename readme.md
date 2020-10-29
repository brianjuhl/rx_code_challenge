# Overview
Code repository for Brian Juhl's solution to the RX Savings Solutions code challenge. Technologies used 
in this project include: 

- Python 3
- FastAPI
- MongoDB
- Docker

# Running Locally
First make sure [Docker and Docker Compose](https://docs.docker.com/get-docker/) are installed on your machine. 

Once Docker is configured, simply pull down the code, ```bash cd``` into the project directory and run ```bash docker-compose up -d --build``` to build and start the containers.

Next you'll need to seed the database with the provided list of pharamacies. 
```bash docker exec rx_code_challenge_api python -m pharmacies.data.seeder```

To ensure everything has been configured properly, the project's tests can be run with: 
```bash docker exec -it rx_code_challenge_api green -vvv -r```

The tests should all pass and you should now be able to access this project's interactive API docs at [localhost:5000/docs](http://localhost:5000/docs)

If you woud like the project to map to a different port, this can be modified in the docker-compose.yml file 
at the root of the project. 

You will need to run ```bash docker-compose up -d --build``` again for any changes to take effect. You do not need to run the seeder again. 

If you would like to restart the container with a new volume (erasing the data added by the seeder) adding the ```bash -V``` flag to ```bash docker-compose up -d --build``` will do so.