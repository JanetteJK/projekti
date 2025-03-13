import random
class Rahapussi_oma:
    def __init__(self):
        self.raha = 0  # Alussa rahaa 0e

    def lisaa_rahaa_oma(self, maara):
        self.raha += maara
        return self.raha #lisää täs rahat olemassa olevaa saldoo (0e)

    def hae_saldo_oma(self):
        return self.raha #palauttaa nykysen saldon kun taso päättyy eli näyttää rahanmäärän

rahapussi = Rahapussi_oma()

import mysql.connector



def get_db_connection_oma():
    return mysql.connector.connect(
        host="localhost",
        port=3306,
        user="root",
        password="niittykuja4MAR",
        database="flight_game",
        collation='latin1_swedish_ci',
        autocommit=True
    )

def get_persons_oma ():
        conn = get_db_connection_oma()
        cursor = conn.cursor()
        cursor.execute("SELECT ID, nimi, difficulty FROM person")
        persons = cursor.fetchall()
        conn.close()
        return persons

def uusi_asiakas_oma(nimi):
    conn = get_db_connection_oma()
    cursor = conn.cursor()
    query = "SELECT ID, nimi, difficulty FROM person WHERE nimi = nimi"
    cursor.execute(query, (nimi,))
    person = cursor.fetchall()
    conn.close()
    return person

tulos = get_persons_oma()
for rivi in tulos:
    print(rivi)
#result = uusi_asiakas('Pauli Pomottelija')
#print(result)


def hae_kysymys_oma(person_id, order_no):
    conn = get_db_connection_oma()
    cursor = conn.cursor()
    query = "SELECT question FROM question WHERE person_id = %s AND Order_No = %s"
    cursor.execute(query, (person_id, order_no))
    kysymys = cursor.fetchone()
    conn.close()
    return kysymys[0] if kysymys else None


def hae_oikea_vastaus_oma(person_id):
    conn = get_db_connection_oma()
    cursor = conn.cursor()
    query = "SELECT answer FROM answer WHERE person_id = %s AND correct = 1"
    cursor.execute(query, (person_id,))
    oikea_vastaus = cursor.fetchone()
    conn.close()
    return oikea_vastaus[0] if oikea_vastaus else None


def hae_asiakkaan_nimi_oma(person_id):
    conn = get_db_connection_oma()
    cursor = conn.cursor()
    query = "SELECT nimi FROM person WHERE id = %s"
    cursor.execute(query, (person_id,))
    nimi = cursor.fetchone()
    conn.close()
    return nimi[0] if nimi else None


def valikko_kohteet_oma():
    try:
        conn = get_db_connection_oma()
        cursor = conn.cursor()

        cursor.execute("SELECT name FROM country ORDER BY RAND() LIMIT 9")
        countries = cursor.fetchall()

        answers = cursor.fetchall()

        results = []
        for country_name in country_names:
            matching_answers = [a for a in answers if a.get('country_name') == country_name]
            answer_info = matching_answers[0] if matching_answers else {"person_id": None, "answer": None,
                                                                        "correct": None}

            results.append({
                "country_name": country_name,
                "person_id": answer_info["person_id"],
                "answer": answer_info["answer"],
                "correct": answer_info["correct"]
            })

        random.shuffle(results)
        return results

    except mysql.connector.Error as error:
        print(f"Error connecting to MySQL database: {error}")
        return []

def main_oma():
    results = valikko_kohteet_oma()
    print(f"{results}")

if __name__ == "__main__":
    main_oma()




def aloita_peli_oma():
    person_id = 1
    order_no = 1
    yritykset = 0
    max_yritykset = 3

    while yritykset < max_yritykset:
        asiakas_nimi = hae_asiakkaan_nimi_oma(person_id)
        oikea_vastaus = hae_oikea_vastaus_oma(person_id)
        kysymys = hae_kysymys_oma(person_id, order_no)
        if person_id > 10 and rahapussi.raha < 100:
            print("Olet oikea asiakaspalvelun ammattilainen! Nyt voit lähteä ansaitsemillasi rahoilla kesälomalle.")
            break
        elif person_id > 11:
            print("tässä hassu bonuslopetus") #tähän joku kiva hassu juttu
            break
        print(f"\n{asiakas_nimi}:\n{kysymys}")
        vastaus = input("Kirjoita matkakohde:\n ").strip()
        if vastaus.lower() == oikea_vastaus.lower():
            if yritykset == 0:
                rahapussi.lisaa_rahaa_oma(15)
                print("\nSaat 10€ tippiä nopeasta vastauksesta!")
                print(f"Hyvää työtä! Ansaitsit 5€.")
                print(f"\nRahapussissasi on nyt {rahapussi.hae_saldo_oma()}€.")
                person_id +=1
                order_no=1
                yritykset=0
            else:
                rahapussi.lisaa_rahaa_oma(5)
                print(f"\nHyvää työtä! Palkkasi on 5€.")
                print(f"Rahapussissasi on nyt {rahapussi.hae_saldo_oma()}€.")
                person_id +=1
                order_no=1
                yritykset=0


        else:
            yritykset += 1
            order_no += 1

    viimeinen_vastaus = hae_kysymys_oma(person_id, 4)
    if yritykset == 3:
        print(f"\n{asiakas_nimi}: {viimeinen_vastaus}")
        print("\nAsiakaspalvelusi oli ala-arvoista ja sait potkut. Voit yrittää uudelleen!")



if __name__ == "__main__":
    aloita_peli_oma()

