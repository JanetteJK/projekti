import mysql.connector

def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        port=3306,
        user="lauri1",
        password="Kukkokiekuu1",
        database="flight_game",
        collation='latin1_swedish_ci',
        autocommit=True
    )
