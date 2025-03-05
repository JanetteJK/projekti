import mysql.connector

def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="käyttäjänimi",
        password="salasana",
        database="tietokannan_nimi"
    )

#muodostaa yhteyden tietokantaan