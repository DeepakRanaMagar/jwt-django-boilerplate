# Base Image -> Docker Image
FROM python:3.9.19-bullseye 

# Setting working directory in Docker
WORKDIR /jwt-django-tutorial

COPY . . 

# Execute on top of the current image as a new layer and commit the results.
RUN pip install -r requirements/requirements-dev.txt


CMD ["python", "manage.py", "runserver"]