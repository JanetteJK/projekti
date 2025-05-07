import mysql.connector

def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        port=3306,
        user="root",
        password="niittykuja4MAR",
        database="flight_game",
        collation='latin1_swedish_ci',
        autocommit=True
    )

def get_persons ():
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT ID, nimi, difficulty FROM person")
        persons = cursor.fetchall()
        conn.close()
        return persons

def uusi_asiakas(nimi):
    conn = get_db_connection()
    cursor = conn.cursor()
    query = "SELECT ID, nimi, difficulty FROM person WHERE nimi = {nimi}"
    cursor.execute(query, (nimi,))
    person = cursor.fetchall()
    conn.close()
    return person

tulos = get_persons()
for rivi in tulos:
    print(rivi)
#result = uusi_asiakas('Pauli Pomottelija')
#print(result)