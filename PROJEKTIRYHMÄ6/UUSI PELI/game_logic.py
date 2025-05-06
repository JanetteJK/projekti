from db_functions import hae_kysymys, hae_vastaus, hae_nimi


class Rahapussi:
    def __init__(self):
        self.rahat = 0

    def lisaa_rahaa(self, maara):
        self.rahat += maara

    def nayta_rahat(self):
        return self.rahat


# Globaalit muuttujat pelitilaa varten
peli_rahapussi = Rahapussi()
peli_henkilo_id = 1
peli_jarjestys = 1
peli_yritykset = 0
peli_max_yritykset = 3
peli_loppui = False
peli_viesti = ""
peli_onnistui = False


def aloita_peli():
    global peli_rahapussi, peli_henkilo_id, peli_jarjestys, peli_yritykset, peli_loppui, peli_viesti, peli_onnistui
    peli_rahapussi = Rahapussi()
    peli_henkilo_id = 1
    peli_jarjestys = 1
    peli_yritykset = 0
    peli_loppui = False
    peli_viesti = ""
    peli_onnistui = False


def hae_pelitila():
    return {
        "nimi": hae_nimi(peli_henkilo_id),
        "kysymys": hae_kysymys(peli_henkilo_id, peli_jarjestys),
        "rahat": peli_rahapussi.nayta_rahat(),
        "yritykset": peli_yritykset,
        "max_yritykset": peli_max_yritykset,
        "peli_loppui": peli_loppui,
        "viesti": peli_viesti,
        "onnistui": peli_onnistui
    }


def tarkista_vastaus(vastaus):
    global peli_henkilo_id, peli_jarjestys, peli_yritykset, peli_loppui, peli_viesti, peli_onnistui

    peli_viesti = ""
    peli_onnistui = False
    oikea_vastaus = hae_vastaus(peli_henkilo_id)

    if vastaus.lower() == oikea_vastaus.lower():
        peli_onnistui = True

        if peli_yritykset == 0:
            peli_rahapussi.lisaa_rahaa(15)
            peli_viesti = "Saat 10€ tippiä nopeasta vastauksesta!\nHyvää työtä! Ansaitsit 5€."
        else:
            peli_rahapussi.lisaa_rahaa(5)
            peli_viesti = "Hyvää työtä! Palkkasi on 5€."

        peli_henkilo_id += 1
        peli_jarjestys = 1
        peli_yritykset = 0

        if peli_henkilo_id > 10 and peli_rahapussi.nayta_rahat() < 100:
            peli_viesti += "\nOlet oikea asiakaspalvelun ammattilainen! Nyt voit lähteä ansaitsemillasi rahoilla kesälomalle."
            peli_loppui = True
        elif peli_henkilo_id > 11:
            peli_viesti += "\nOnneksi olkoon! Olet päässyt pelin loppuun."
            peli_loppui = True

        return True
    else:
        peli_yritykset += 1
        peli_jarjestys += 1

        if peli_yritykset >= peli_max_yritykset:
            loppu_kysymys = hae_kysymys(peli_henkilo_id, 4)
            asiakas_nimi = hae_nimi(peli_henkilo_id)
            peli_viesti = f"{asiakas_nimi}: {loppu_kysymys}\n\nAsiakaspalvelusi oli ala-arvoista ja sait potkut. Voit yrittää uudelleen!"
            peli_loppui = True

        return False