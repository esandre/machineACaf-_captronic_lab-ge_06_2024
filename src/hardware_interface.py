import abc


class HardwareInterface(abc.ABC):
    @abc.abstractmethod
    def est_defaillant(self) -> bool:
        pass
