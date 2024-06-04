from machine_a_café import MachineACafé
from machine_a_café_interface import MachineACaféInterface
from utilities.hardware_dummy import HardwareDummy
from utilities.hardware_stub import HardwareStub
from typing import Self

from utilities.machine_a_café_harness import MachineACaféHarness


class MachineACaféBuilder:
    __est_défaillante = False

    @classmethod
    def par_defaut(cls):
        return MachineACaféBuilder().build()

    def build(self) -> MachineACaféInterface:
        hardware = HardwareDummy() if self.__est_défaillante else HardwareStub()
        return MachineACaféHarness(MachineACafé(hardware))

    def défaillante(self) -> Self:
        self.__est_défaillante = True
        return self
