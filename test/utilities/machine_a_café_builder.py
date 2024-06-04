from machine_a_café import MachineACafé
from utilities.hardware_défaillant import HardwareDéfaillant
from utilities.hardware_quelconque import HardwareQuelconque


class MachineACaféBuilder:
    __est_défaillante = False

    @classmethod
    def par_defaut(cls):
        return MachineACaféBuilder().build()

    def build(self) -> MachineACafé:
        hardware = HardwareDéfaillant() if self.__est_défaillante else HardwareQuelconque()
        return MachineACafé(hardware)

    def défaillante(self):
        self.__est_défaillante = True
        return self
