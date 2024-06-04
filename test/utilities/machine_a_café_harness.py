from machine_a_café_interface import MachineACaféInterface
from utilities.hardware_spy import HardwareSpy


class MachineACaféHarness(MachineACaféInterface):
    def get_somme_encaissée_en_centimes(self):
        return self.__machine.get_somme_encaissée_en_centimes()

    def __init__(self, machine: MachineACaféInterface, hardwareSpy: HardwareSpy):
        self.__hardwareSpy = hardwareSpy
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
