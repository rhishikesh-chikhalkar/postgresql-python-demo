import psycopg2
import configparser

config = configparser.ConfigParser()
config.read("db_config.ini")

database = config["postgreSQLDB"]["database"]
hostname = config["postgreSQLDB"]["hostname"]
port = config["postgreSQLDB"]["port"]
uid = config["postgreSQLDB"]["uid"]
pwd = config["postgreSQLDB"]["pwd"]


def db_connect():
    conn = None
    try:
        conn_string = (
            f"host={hostname} port={port} dbname={database} user={uid} password={pwd}"
        )
        conn = psycopg2.connect(conn_string)
        cursor = conn.cursor()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    return conn, cursor
