from pièce import Pièce


class MachineACafé:
    def __init__(self):
        self.somme_encaissée_en_centimes = 0
        self.nombre_cafés_servis = 0

    def insérer(self, montant):
        if montant < Pièce.UnEuro: return

        self.somme_encaissée_en_centimes += montant
        self.nombre_cafés_servis += 1
