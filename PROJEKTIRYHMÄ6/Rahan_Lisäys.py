class Rahapussi:
    def __init__(self):
        self.raha = 0  # Alussa rahaa 0e

    def lisaa_rahaa(self, maara):
        self.raha += maara
        return self.raha #lisää täs rahat olemassa olevaa saldoo (0e)

    def hae_saldo(self):
        return self.raha #palauttaa nykysen saldon kun taso päättyy eli näyttää rahanmäärän

