import mysql.connector

def get_db_connection():
    return mysql.connector.connect(
        host="127.0.0.1",
        port=3306,
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

get_persons()
def uusi_asiakas(nimi):
    person= f'SELECT ID, nimi, difficulty from person where nimi={nimi}'
    print(person)
    return
uusi_asiakas('Pauli Pomottelija')

