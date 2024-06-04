import machine_a_café_interface
from hardware_interface import HardwareInterface
from pièce import Pièce


class MachineACafé(machine_a_café_interface.MachineACaféInterface):
    def __init__(self, hardware: HardwareInterface):
        self.somme_encaissée_en_centimes = 0
        self.__hardware = hardware

    def insérer(self, montant):
        if montant < Pièce.UnEuro: return
        if self.__hardware.est_defaillant(): return

        self.somme_encaissée_en_centimes += montant
        self.__hardware.couler_un_café()
