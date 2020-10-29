# Overview
Code repository for Brian Juhl's solution to the RX Savings Solutions code challenge. Technologies used 
in this project include: 

- Python 3
- FastAPI
- MongoDB
- Docker

# Running Locally
First make sure [Docker and Docker Compose](https://docs.docker.com/get-docker/) are installed on your machine. 

Once Docker is configured, simply pull down the code, ```cd``` into the project directory and build and start the containers.

``` docker-compose up -d --build```

Next you'll need to seed the database with the provided list of pharamacies. 

```docker exec rx_code_challenge_api python -m pharmacies.data.seeder```

To ensure everything has been configured properly, run the project's tests.

```docker exec -it rx_code_challenge_api green -vvv -r```

The tests should all pass and you should now be able to access this project's interactive API docs at [localhost:5000/docs](http://localhost:5000/docs)

If you woud like the project to map to a different port, this can be modified in the docker-compose.yml file 
at the root of the project. 

To stop the containers and remove the volume used by the mongodb service run:

```docker-compose down -v```