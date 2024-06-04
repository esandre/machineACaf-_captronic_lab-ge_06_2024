import abc


class HardwareInterface(abc.ABC):
    @abc.abstractmethod
    def est_defaillant(self) -> bool:
        pass

    @abc.abstractmethod
    def couler_un_café(self):
        pass
