# Base Image -> Docker Image
FROM python:3.9.19-bullseye 

# Setting working directory in Docker
WORKDIR /src

# copying the code from the local storage to the docker WORKDIR
COPY requirements/requirements-dev.txt .

# Execute on top of the current image as a new layer and commit the results.
RUN pip install -r requirements-dev.txt

COPY . . 

CMD ["python", "manage.py", "runserver"]