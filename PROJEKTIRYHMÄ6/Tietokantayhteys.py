import mysql.connector

def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="lauri1",
        password="Kukkokiekuu1",
        database="flight_game",
        autocommit=True
    )

def get_persons ():
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT ID, nimi, difficulty FROM person")
        persons = cursor.fetchall()
        conn.close()
        return persons
