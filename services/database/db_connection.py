# services/database/db_connection.py
import psycopg2


def connect_to_db():
    try:
        conn = psycopg2.connect(
            host="localhost",
            database="magic_db",
            user="your_username",
            password="your_password"
        )
        return conn
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)


def close_connection(conn):
    if conn is not None:
        conn.close()
