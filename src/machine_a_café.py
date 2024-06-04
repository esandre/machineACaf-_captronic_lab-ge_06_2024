class MachineACafé:
    def __init__(self):
        self.somme_encaissée_en_centimes = 0
        self.nombre_cafés_servis = 0

    def insérer(self, montant):
        self.somme_encaissée_en_centimes += montant
        self.nombre_cafés_servis += 1
