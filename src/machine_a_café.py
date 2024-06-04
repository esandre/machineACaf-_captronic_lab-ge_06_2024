from hardware_interface import HardwareInterface
from pièce import Pièce


class MachineACafé:
    def __init__(self, hardware: HardwareInterface):
        self.somme_encaissée_en_centimes = 0
        self.nombre_cafés_servis = 0
        self.__hardware = hardware

    def insérer(self, montant):
        if montant < Pièce.UnEuro: return
        if self.__hardware.est_defaillant(): return

        self.somme_encaissée_en_centimes += montant
        self.nombre_cafés_servis += 1
