from Rahan_Lisäys import Rahapussi
from Tietokantayhteys import get_db_connection
rahapussi = Rahapussi()


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


def aloita_peli():
    person_id = 1
    order_no = 1
    yritykset = 0
    max_yritykset = 3

    asiakas_nimi = hae_asiakkaan_nimi(person_id)
    oikea_vastaus = hae_oikea_vastaus(person_id)

    while yritykset < max_yritykset:
        kysymys = hae_kysymys(person_id, order_no)
        if not kysymys:
            print("Peli päättyi.")
            return

        print(f"\n{asiakas_nimi}: {kysymys}")
        vastaus = input("Kirjoita matkakohde: ").strip()

        if vastaus.lower() == oikea_vastaus.lower():
            if yritykset == 0:
                rahapussi.lisaa_rahaa(15)
                print("Saat 10€ tippiä nopeasta vastauksesta!")
            else:
                rahapussi.lisaa_rahaa(5)
                print(f"\nHyvää työtä! Ansaitsit 5€.")

            print(f"Rahapussissasi on nyt {rahapussi.hae_saldo()}€.")
            return
        else:
            yritykset += 1
            order_no += 1

    viimeinen_kysymys = hae_kysymys(person_id, 4)
    if viimeinen_kysymys:
        print(f"\n{asiakas_nimi}: {viimeinen_kysymys}")

    print("Peli päättyi. Voit yrittää uudelleen!") # Tää alue vaihdetaan sitten tietokantadataan eli pitää keksi miten sinne laitetaan oikean vastauksen dialogit!



if __name__ == "__main__":
    aloita_peli()

