# simple-pipeline

## Overview

This simple project provide a simple data pipline

## Features

* Transform and Loading base on config file
* Decoupling service
* Easy to startup
* Schema migratioin
* Provide Upserted

## Services
* Transform service: Transform `raw_data` to `modelled_data`
* Loader service: Load `modelled_data` to database
* Database: postgres
* Schema Migration: Alembic

## How to start?

To start whole service run this cmd
```bash
make deploy
```

## Run pipeline
```bash
sh ./run_test.sh $src $date
```

## Check the database

Go to `localhost:8080` sign in with this auth to check pipeline is work correctly. Table: `public.users`:
* `System` : PostgreSQL
* `server` : postgres
* `Username` : postgres
* `Password` : postgres
* `Database` : postgres

## Further Improvement

1. Refactor code to be more easily to maintain
1. Add Testcase
1. With http_transport need to implement an Load ballancer service to scale transform and loader service

