#jos sinulla on 100+ rahaa saat bonuskentän
from Rahan_Lisäys import Rahapussi

rahapussi = Rahapussi()

def bonus_tarkistus():
    rahat = rahapussi.hae_saldo()
    if rahat >= 100:
        person_id = 11
        order_no = 1
    return
