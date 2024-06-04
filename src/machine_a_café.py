import machine_a_café_interface
from hardware_interface import HardwareInterface
from lecteur_cb_interface import LecteurCbInterface, CarteDétectée
from pièce import Pièce


class MachineACafé(machine_a_café_interface.MachineACaféInterface):
    def get_somme_encaissée_en_centimes(self):
        return self.somme_encaissée_en_centimes

    def __init__(self, hardware: HardwareInterface, lecteur_cb: LecteurCbInterface):
        self.somme_encaissée_en_centimes = 0
        self.__hardware = hardware
        lecteur_cb.register(self.__débiter)

    def __débiter(self, carte: CarteDétectée):
        succes = carte.tenter_debit(70)
        if succes:
            self.__hardware.couler_un_café()

    def insérer(self, montant):
        if montant < Pièce.UnEuro: return
        if self.__hardware.est_defaillant(): return

        self.somme_encaissée_en_centimes += montant
        self.__hardware.couler_un_café()