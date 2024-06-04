from machine_a_café_interface import MachineACaféInterface


class MachineACaféHarness(MachineACaféInterface):
    def get_somme_encaissée_en_centimes(self):
        return self.__machine.get_somme_encaissée_en_centimes()

    def __init__(self, machine: MachineACaféInterface):
        self.__machine = machine

    def insérer(self, montant):
        return self.__machine.insérer(montant)