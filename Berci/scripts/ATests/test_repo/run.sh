#!/bin/bash

DB_ADDRESS=${DB_ADDRESS:-"127.0.0.1"}
DB_PORT=${DB_PORT:-"5432"}
POSTGRES_USER=${POSTGRES_USER:-"postgres"}
POSTGRES_PASSWORD=${POSTGRES_PASSWORD:-"postgres"}

DB_NAME="core_customer"
STEP1="$DB_NAME/liquibase-install-db1-step-01.xml"
STEP2="$DB_NAME/liquibase-install-db1-step-02.xml"

./liquibase \
    --logLevel=info \
    --liquibase-hub-mode=off \
    --driver=org.postgresql.Driver \
    --username=postgres \
    --password="$POSTGRES_PASSWORD" \
    --classpath=./changelog \
    --url=jdbc:postgresql://$DB_ADDRESS:$DB_PORT/postgres \
    --changelogfile=$STEP1 \
    update 2>&1

./liquibase \
    --logLevel=info \
    --liquibase-hub-mode=off \
    --driver=org.postgresql.Driver \
    --username=postgres \
    --password="$POSTGRES_PASSWORD" \
    --classpath=./changelog \
    --url=jdbc:postgresql://$DB_ADDRESS:$DB_PORT/$DB_NAME \
    --changelogfile=$STEP2 \
    update 2>&1
