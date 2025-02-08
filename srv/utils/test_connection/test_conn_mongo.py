from pymongo import MongoClient
from srv.utils.test_connection.config  import settings


def test_connection():

    client = MongoClient(settings.uri_mongodb)

    try:
        client.admin.command("ping")
        print("Syccesfuull connection")
    except Exception as e:
        print(f"❌ Error connection: {e}")
    finally:
        client.close()

if __name__ == "__main__":
    test_connection()
