import os

# Get the SQS queue URL from an environment variable
SQS_QUEUE_URL = os.environ.get("SQS_QUEUE_URL", "http://localhost:4566/000000000000/login-queue")

# PostgreSQL connection parameters from environment variables
POSTGRES_CONNECTION = {
    "dbname": os.environ.get("POSTGRES_DBNAME", "postgres"),
    "user": os.environ.get("POSTGRES_USER", "postgres"),
    "password": os.environ.get("POSTGRES_PASSWORD", "postgres"),
    "host": os.environ.get("POSTGRES_HOST", "localhost"),
    "port": int(os.environ.get("POSTGRES_PORT", 5432)),
}
