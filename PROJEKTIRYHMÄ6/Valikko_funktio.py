from Rahan_Lisäys import Rahapussi
from Tietokantayhteys import get_db_connection
import random
import mysql.connector

rahapussi = Rahapussi()


def get_db_connection_oma():
    return get_db_connection()


def hae_kysymys(person_id, order_no):
    conn = get_db_connection()
    cursor = conn.cursor()
    query = "SELECT question FROM question WHERE person_id = %s AND Order_No = %s"
    cursor.execute(query, (person_id, order_no))
    kysymys = cursor.fetchone()
    conn.close()
    return kysymys[0] if kysymys else None


def hae_oikea_vastaus(person_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    query = "SELECT answer FROM answer WHERE person_id = %s AND correct = 1"
    cursor.execute(query, (person_id,))
    oikea_vastaus = cursor.fetchone()
    conn.close()
    return oikea_vastaus[0] if oikea_vastaus else None


def hae_asiakkaan_nimi(person_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    query = "SELECT nimi FROM person WHERE id = %s"
    cursor.execute(query, (person_id,))
    nimi = cursor.fetchone()
    conn.close()
    return nimi[0] if nimi else None


def hae_valikko_kohteet(person_id):
    try:
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)

        oikea_vastaus = hae_oikea_vastaus(person_id)

        # täs hakee random järjestykses ne 9 extraa tietokannast
        cursor.execute("SELECT name FROM country ORDER BY RAND() LIMIT 9")
        countries = cursor.fetchall()

        # varmistetaa et tulee vaan maan nimi näkyvii
        country_names = [country['name'] for country in countries]

        # varmistetaa ettei tuu tuplia listoille, se olis kyl funny tho
        if oikea_vastaus not in country_names:
            if country_names:
                country_names.pop()
            country_names.append(oikea_vastaus)

        # haetaa vastaustiedot kaikille maille
        format_strings = ','.join(['%s'] * len(country_names))
        cursor.execute(
            f"SELECT country.name AS country_name, person_id, answer, correct FROM answer "
            f"JOIN country ON answer.country_id = country.id "
            f"WHERE country.name IN ({format_strings})",
            country_names)
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

        # mix ts up
        random.shuffle(results)

        conn.close()
        return results

    except mysql.connector.Error as error:
        print(f"Error connecting to MySQL database: {error}")
        return []


# allegedly listaa sit pelaajalle
def nayta_valikko(valikko_kohteet):
    print("\nValitse oikea matkakohde:")
    for i, kohde in enumerate(valikko_kohteet, 1):
        print(f"{i}. {kohde['country_name']}")


def aloita_peli_oma():
    person_id = 1
    order_no = 1
    yritykset = 0
    max_yritykset = 3

    while yritykset < max_yritykset:
        asiakas_nimi = hae_asiakkaan_nimi(person_id)
        oikea_vastaus = hae_oikea_vastaus(person_id)
        kysymys = hae_kysymys(person_id, order_no)

        # sormet ristii tjtn
        valikko_kohteet = hae_valikko_kohteet(person_id)

        if person_id > 10 and rahapussi.raha >= 100:
            print("Olet oikea asiakaspalvelun ammattilainen! Nyt voit lähteä ansaitsemillasi rahoilla kesälomalle.")
            break
        elif person_id > 11:
            print("Tässä hassu bonuslopetus")  # tähän joku kiva hassu juttu
            break

        print(f"\n{asiakas_nimi}:\n{kysymys}")

        nayta_valikko(valikko_kohteet)

        vastaus_input = input("Anna vastauksesi (numero tai kirjoita): ").strip()

        # ignore tää lowkey, checkkaa et mitä jos pelaaja ois vastannu numerolla
        if vastaus_input.isdigit() and 1 <= int(vastaus_input) <= len(valikko_kohteet):
            vastaus = valikko_kohteet[int(vastaus_input) - 1]['country_name']
        else:
            vastaus = vastaus_input

        if vastaus.lower() == oikea_vastaus.lower():
            if yritykset == 0:
                rahapussi.lisaa_rahaa(15)
                print("\nSaat 10€ tippiä nopeasta vastauksesta!")
                print(f"Hyvää työtä! Ansaitsit 5€.")
                print(f"\nRahapussissasi on nyt {rahapussi.hae_saldo()}€.")
                person_id += 1
                order_no = 1
                yritykset = 0
            else:
                rahapussi.lisaa_rahaa(5)
                print(f"\nHyvää työtä! Palkkasi on 5€.")
                print(f"Rahapussissasi on nyt {rahapussi.hae_saldo()}€.")
                person_id += 1
                order_no = 1
                yritykset = 0
        else:
            yritykset += 1
            order_no += 1
            print(f"Väärä vastaus! Yrityksiä jäljellä: {max_yritykset - yritykset}")

    viimeinen_vastaus = hae_kysymys(person_id, 4)
    if yritykset == max_yritykset:
        print(f"\n{asiakas_nimi}: {viimeinen_vastaus}")
        print("\nAsiakaspalvelusi oli ala-arvoista ja sait potkut. Voit yrittää uudelleen!")


if __name__ == "__main__":
    aloita_peli_oma()