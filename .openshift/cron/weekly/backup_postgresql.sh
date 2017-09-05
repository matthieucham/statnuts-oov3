#!/bin/bash
# Backs up the OpenShift PostgreSQL database for this application
# by Skye Book <skye.book@gmail.com>

NOW="$(date +"%Y-%m-%d")"
FILENAME="$OPENSHIFT_DATA_DIR/$OPENSHIFT_APP_NAME.$NOW.backup.gz"
pg_dump -F t -U $PGUSER -h $OPENSHIFT_POSTGRESQL_DB_HOST $OPENSHIFT_APP_NAME | gzip > $FILENAME