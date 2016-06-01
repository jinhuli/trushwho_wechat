#!/bin/bash
APP_LOCATION=/home/likun/app/trustwho
cd $APP_LOCATION
source /home/likun/env/bin/activate
python manage.py celery worker -B -l info >> $APP_LOCATION/logs/task.log 2>&1 &
