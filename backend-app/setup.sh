#!/bin/bash

# /code/backend-appがDockerfileのWORKDIR
cd /code/backend-app/djangoApp

python3 manage.py migrate
python3 manage.py createsuperuser --noinput
# python3 manage.py runserver 0.0.0.0:8000
bash