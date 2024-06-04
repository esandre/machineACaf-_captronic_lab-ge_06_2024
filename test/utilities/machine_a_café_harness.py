from machine_a_café_interface import MachineACaféInterface
from utilities.fake_lecteur_cb import FakeLecteurCb
from utilities.hardware_spy import HardwareSpy


class MachineACaféHarness(MachineACaféInterface):
    def get_somme_encaissée_en_centimes(self):
        return self.__machine.get_somme_encaissée_en_centimes()

    def __init__(self, machine: MachineACaféInterface, hardware_spy: HardwareSpy, lecteur_cb_fake: FakeLecteurCb):
        self.__lecteur_cb_fake = lecteur_cb_fake
        self.__hardwareSpy = hardware_spy
        self.__machine = machine
        self.__argentEncaisséInitial = machine.get_somme_encaissée_en_centimes()

    def insérer(self, montant):
        return self.__machine.insérer(montant)

    def couler_un_café_appelé(self):
        return self.__hardwareSpy.couler_un_café_appelé()

    def get_delta_argent_encaissé(self):
        return self.get_somme_encaissée_en_centimes() - self.__argentEncaisséInitial

    def nombre_appels_a_couler_un_café(self):
        return self.__hardwareSpy.nombre_appels_a_couler_un_café()

    def simuler_présentation_carte(self):
        return self.__lecteur_cb_fake.simuler_présentation_carte()

    def get_ordres_débit(self):
        return self.__lecteur_cb_fake.get_ordres_debit()
