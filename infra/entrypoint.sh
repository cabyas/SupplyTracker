#!/bin/bash

echo
echo Starting Supply tracker app\'s container

# set up django stuff
chown -R supply_tracker_usr media
touch /app/logs/errors.log
touch /app/logs/warn.log
chown -R supply_tracker_usr /app/logs/errors.log
chown -R supply_tracker_usr /app/logs/warn.log

echo Collecting statics...
python manage.py collectstatic --no-input
echo Collected statics OK
python manage.py migrate
echo Migrated DB

# execute command passed as parameter
"$@"
