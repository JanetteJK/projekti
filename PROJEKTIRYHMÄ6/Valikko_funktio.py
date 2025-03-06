#tänne valikko joista pelaajan pitää valita oikea vastaus
#oikea vastaus + 9 randomia countries taulusta

#tää ei oo ready, juli vaan säätää tääl hihi <333

from Tietokantayhteys import get_db_connection
import random

def matkakohteet():
    conn = get_db_connection()
    cursor = conn.cursor()
    # future juli -> fixaa toi select-from oikeisiin paskoihin en nyt jaksanu owo
    cursor.execute("SELECT person_id, answer, correct FROM person")
    persons = cursor.fetchall()
    conn.close()
    return

    # täs kohtaa haetaan 9 randomii maata mut en tiiä miten randomisaan
    # tuolt pullatut maat,, PEREHDY JULI!!!
    cursor.execute("SELECT country_id FROM countries ORDER BY rand() LIMIT 9")
    countries = cursor.fetchall()