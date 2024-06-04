from hardware_interface import HardwareInterface


class HardwareDéfaillant(HardwareInterface):
    def est_defaillant(self):
        return True
