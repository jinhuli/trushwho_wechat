#!/bin/bash
APP_LOCATION=/Users/likun/workspace/trustwho/
cd $APP_LOCATION
source /Users/likun/env/1.8/bin/activate
python manage.py celery worker -B -l info >> $APP_LOCATION/logs/task.log 2>&1 &
