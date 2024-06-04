from machine_a_café import MachineACafé
from utilities.hardware_dummy import HardwareDummy
from utilities.hardware_spy import HardwareSpy
from utilities.hardware_stub import HardwareStub
from typing import Self

from utilities.machine_a_café_harness import MachineACaféHarness


class MachineACaféBuilder:
    __est_défaillante = False

    @classmethod
    def par_defaut(cls):
        return MachineACaféBuilder().build()

    def build(self) -> MachineACaféHarness:
        hardware = HardwareDummy() if self.__est_défaillante else HardwareStub()
        hardware_spy = HardwareSpy(hardware)
        return MachineACaféHarness(MachineACafé(hardware_spy), hardware_spy)

    def défaillante(self) -> Self:
        self.__est_défaillante = True
        return self
