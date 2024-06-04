from hardware_interface import HardwareInterface


class HardwareStub(HardwareInterface):
    def couler_un_café(self):
        pass

    def est_defaillant(self):
        return False
