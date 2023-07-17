import psycopg2
from psycopg2.extras import execute_batch

# Function to convert a list of 'Record' objects to a list of tuples
def convert_records_to_tuples(records):
    return [
        (
            record.user_id, record.device_type, record.masked_ip,
            record.masked_device_id, record.locale, record.app_version, record.create_date
        )
        for record in records
    ]

# Function to insert records into the 'user_logins' table in the Postgres database
def insert_to_postgres(connection_params, records):
    # SQL query to create the 'user_logins' table if it doesn't exist
    create_table_query = """
    CREATE TABLE IF NOT EXISTS user_logins (
        user_id VARCHAR(128),
        device_type VARCHAR(32),
        masked_ip VARCHAR(256),
        masked_device_id VARCHAR(256),
        locale VARCHAR(32),
        app_version INTEGER,
        create_date DATE
    );
    """

    # SQL query to insert records into the 'user_logins' table
    insert_query = """
    INSERT INTO user_logins (
        user_id,
        device_type,
        masked_ip,
        masked_device_id,
        locale,
        app_version,
        create_date
    ) VALUES (%s, %s, %s, %s, %s, %s, %s);
    """

    # Connect to the Postgres database
    with psycopg2.connect(**connection_params) as conn:
        with conn.cursor() as cur:
            # Create the table if it doesn't exist
            cur.execute(create_table_query)

            # Convert the Record objects to tuples
            converted_records = convert_records_to_tuples(records)

            # Execute batch insert using execute_batch
            execute_batch(cur, insert_query, converted_records)

        # Commit the transaction
        conn.commit()
