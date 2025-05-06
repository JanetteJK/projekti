import mysql.connector

def yhdista_tietokantaan():
    yhteys = mysql.connector.connect(
        host="localhost",
        port=3306,
        user="root",
        password="pietari9046",
        database="flight_game"
    )
    return yhteys

def hae_henkilot():
    yhteys = yhdista_tietokantaan()
    kursori = yhteys.cursor()
    kursori.execute("SELECT ID, nimi, difficulty FROM person")
    henkilot = kursori.fetchall()
    kursori.close()
    yhteys.close()
    return henkilot

def hae_kysymys(henkilo_id, jarjestys):
    yhteys = yhdista_tietokantaan()
    kursori = yhteys.cursor()
    kursori.execute("SELECT question FROM question WHERE person_id = %s AND Order_No = %s",
                  (henkilo_id, jarjestys))
    kysymys = kursori.fetchone()
    kursori.close()
    yhteys.close()
    if kysymys:
        return kysymys[0]
    else:
        return "Kysymystä ei löytynyt"

def hae_nimi(henkilo_id):
    yhteys = yhdista_tietokantaan()
    kursori = yhteys.cursor()
    kursori.execute("SELECT nimi FROM person WHERE id = %s", (henkilo_id,))
    nimi = kursori.fetchone()
    kursori.close()
    yhteys.close()
    if nimi:
        return nimi[0]
    else:
        return "Tuntematon"

def hae_vastaus(henkilo_id):
    yhteys = yhdista_tietokantaan()
    kursori = yhteys.cursor()
    kursori.execute("SELECT answer FROM answer WHERE person_id = %s AND correct = 1", (henkilo_id,))
    vastaus = kursori.fetchone()
    kursori.close()
    yhteys.close()
    if vastaus:
        return vastaus[0]
    else:
        return "Vastausta ei löytynyt"