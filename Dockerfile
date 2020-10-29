FROM tiangolo/uvicorn-gunicorn:python3.7

# set a directory for the app
# WORKDIR /usr/src/app

# copy all the files to the container
COPY ./api /app

# install dependencies
RUN pip install --no-cache-dir -r requirements.txt


