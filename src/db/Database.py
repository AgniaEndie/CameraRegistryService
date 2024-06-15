import psycopg
import os


class DatabaseConnect:
    def conn(self):
        return psycopg.connect(
            f"host=postgres-camera-registry-service port=5432 user=foxstudios dbname={os.environ.get('POSTGRES_DB')} password={os.environ.get('POSTGRES_PASSWORD')}")