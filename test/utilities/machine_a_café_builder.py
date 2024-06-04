from machine_a_café import MachineACafé
from utilities.hardware_dummy import HardwareDummy
from utilities.hardware_stub import HardwareStub
from typing import Self


class MachineACaféBuilder:
    __est_défaillante = False

    @classmethod
    def par_defaut(cls):
        return MachineACaféBuilder().build()

    def build(self) -> MachineACafé:
        hardware = HardwareDummy() if self.__est_défaillante else HardwareStub()
        return MachineACafé(hardware)

    def défaillante(self) -> Self:
        self.__est_défaillante = True
        return self
