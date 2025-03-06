import mysql.connector

def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="lauri1",
        password="Kukkokiekuu1",
        database="flight_game",
        autocommit=True
    )

#muodostaa yhteyden tietokantaan