from hardware_interface import HardwareInterface


class HardwareSpy(HardwareInterface):
    __couler_un_café_appelé = 0

    def couler_un_café(self):
        self.__couler_un_café_appelé += 1

    def est_defaillant(self) -> bool:
        pass

    def couler_un_café_appelé(self):
        return self.__couler_un_café_appelé > 0

    def nombre_appels_a_couler_un_café(self):
        return self.__couler_un_café_appelé