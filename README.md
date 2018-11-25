# matcher-py
Just another small project - matching inputs from results and storing them

# Start up

# Pre-requisites
```
1) Install Docker + docker-compose
2) Prepare init_01_creation.sql and init_02_dumping_data.sql according your model
   2.1) init_01_creation.sql : table creation scripts
   2.2) init_02_dumping_data.sql : dumping data sql_scripts
   2.3) Place *.csv files in sql_scripts folder (initial_sample_data.csv as example)
```

```
docker-compose up
```

If you change your `sql_scripts` you may need see no changes happened.
1) Run `docker-compose down`
2) Try using `--force-recreate` flag when run `docker-compose up` again.
