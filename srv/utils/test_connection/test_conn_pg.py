import psycopg2
from srv.utils.test_connection.config import settings

def postgres_connect():
    try:
        pg_conn = psycopg2.connect(
            user=settings.pg_user,
            password=settings.pg_password,
            dbname=settings.pg_database_name,
            port=settings.pg_port,
            host=settings.pg_host
        )
        print("Connection successful!")
        return pg_conn
    except psycopg2.OperationalError as err:
        print(f"Connection failed: {err}")
        return None

if __name__ == "__main__":
    connection = postgres_connect()
    if connection:
        connection.close()