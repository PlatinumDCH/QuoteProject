from srv.utils.test_connection.config import settings
from pymongo import MongoClient
import psycopg2


def postgres_connect():
    connection = psycopg2.connect(
        dbname = settings.pg_database_name,
        user = settings.pg_user,
        password = settings.pg_password,
        host = settings.pg_host,
        port = settings.pg_port
    )
    return connection

def connect_pymongo():
    client = MongoClient(settings.uri_mongodb)
    db = client['hm']
    return db
