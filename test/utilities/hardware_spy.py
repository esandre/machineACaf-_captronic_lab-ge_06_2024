from hardware_interface import HardwareInterface


class HardwareSpy(HardwareInterface):
    __couler_un_café_appelé = 0

    def __init__(self, comportement: HardwareInterface):
        self.__comportement = comportement

    def couler_un_café(self):
        self.__couler_un_café_appelé += 1
        return self.__comportement.couler_un_café()

    def est_defaillant(self) -> bool:
        return self.__comportement.est_defaillant()

    def couler_un_café_appelé(self):
        return self.__couler_un_café_appelé > 0

    def nombre_appels_a_couler_un_café(self):
        return self.__couler_un_café_appelé
