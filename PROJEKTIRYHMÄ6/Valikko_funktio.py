#tänne valikko joista pelaajan pitää valita oikea vastaus
#oikea vastaus + 9 randomia countries taulusta

#tää ei oo done viel, juli säätää tääl

#SQL yhteydes joku ongelma

import mysql.connector
from Tietokantayhteys import get_db_connection
import random

def valikko_kohteet_oma():
    try:
        conn = get_db_connection_oma()
        cursor = conn.cursor(dictionary=True)

        cursor.execute("SELECT name FROM country ORDER BY RAND() LIMIT 9")
        countries = cursor.fetchall()

        country_names = [country['name'] for country in countries]

        # käytetään maan nimi instead of country_id myöhemmin
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

        random.shuffle(results)
        return results

    except mysql.connector.Error as error:
        print(f"Error connecting to MySQL database: {error}")
        return []

def main_oma():
    results = valikko_kohteet()
    print(f"{results}")

if __name__ == "__main__":
    main()