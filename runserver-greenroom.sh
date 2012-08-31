#!/bin/bash
mkdir -p /tmp/static
mkdir -p /tmp/media
./manage.py collectstatic -i sass
./manage.py runserver --nostatic
