# Fetch Rewards #
## Data Engineering Take Home: ETL off a SQS Qeueue ##
```link
https://fetch-hiring.s3.amazonaws.com/data-engineer/pii-masking.pdf
```

## To run the code
1. Run Docker-compose.yml file
```cmd
docker-compose up -d
```

2. Run Python main.py file
```python
python -m app.main
```

3. Run to connect to the Postgres database
```cmd
psql -d postgres -U postgres -p 5432 -h localhost -W
```

4. Run SQL for showing all contents 
```postgres
select * from user_logins
```

## Credentials and database information
1. **username**=`postgres`
2. **password**=`postgres`
3. **database**=`postgres`
