from lecteur_cb_interface import AucunLecteurCb
from machine_a_café import MachineACafé
from utilities.fake_lecteur_cb import FakeLecteurCb
from utilities.hardware_dummy import HardwareDummy
from utilities.hardware_spy import HardwareSpy
from utilities.hardware_stub import HardwareStub
from typing import Self

from utilities.machine_a_café_harness import MachineACaféHarness


class MachineACaféBuilder:
    __est_défaillante = False
    __avec_lecteur_cb = False

    @classmethod
    def par_defaut(cls):
        return MachineACaféBuilder().build()

    def build(self) -> MachineACaféHarness:
        hardware = HardwareDummy() if self.__est_défaillante else HardwareStub()
        hardware_spy = HardwareSpy(hardware)

        lecteur_cb = FakeLecteurCb() if self.__avec_lecteur_cb else AucunLecteurCb()
        return MachineACaféHarness(MachineACafé(hardware_spy, lecteur_cb), hardware_spy, lecteur_cb)

    def défaillante(self) -> Self:
        self.__est_défaillante = True
        return self

    def ayant_un_lecteur_cb(self) -> Self:
        self.__avec_lecteur_cb = True
        return self
