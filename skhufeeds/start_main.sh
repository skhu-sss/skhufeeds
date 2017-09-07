#!/bin/sh

python3 manage.py makemigrations skhufeeds
python3 manage.py makemigrations settings
python3 manage.py makemigrations crawlers
python3 manage.py migrate
gunicorn -b 0.0.0.0:3000 skhufeeds.wsgi
