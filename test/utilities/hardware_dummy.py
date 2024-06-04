from hardware_interface import HardwareInterface


class HardwareDummy(HardwareInterface):
    def couler_un_café(self):
        pass

    def est_defaillant(self):
        return True
