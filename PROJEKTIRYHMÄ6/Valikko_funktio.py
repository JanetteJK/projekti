#tänne valikko joista pelaajan pitää valita oikea vastaus
#oikea vastaus + 9 randomia countries taulusta

#tää ei oo done viel, juli säätää tääl

#SQL yhteydes joku ongelma

import mysql.connector
from Tietokantayhteys import get_db_connection
import random


def valikko_kohteet():
    try:
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)

        # onks tää yhteys oikein?
        # tähän pitää myös vielä lisätä et hakee sen yhden oikeen vastauksen sekaan
        cursor.execute("SELECT country_id FROM countries ORDER BY RAND() LIMIT 9")
        countries = cursor.fetchall()

        country_ids = [country['country_id'] for country in countries]

        format_strings = ','.join(['%s'] * len(country_ids))
        cursor.execute(
            f"SELECT person_id, answer, correct, country_id FROM answer WHERE country_id IN ({format_strings})",
            country_ids)
        answers = cursor.fetchall()

        results = []
        for country_id in country_ids:
            matching_answers = [a for a in answers if a.get('country_id') == country_id]
            answer_info = matching_answers[0] if matching_answers else {"person_id": None, "answer": None,
                                                                        "correct": None}

            results.append({
                "country_id": country_id,
                "person_id": answer_info["person_id"],
                "answer": answer_info["answer"],
                "correct": answer_info["correct"]
            })

        random.shuffle(results)
        return results

    except mysql.connector.Error as error:
        print(f"Error connecting to MySQL database: {error}")
        return []

def main():
    results = valikko_kohteet()
    print(f"{results}")

if __name__ == "__main__":
    main()