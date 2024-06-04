import abc


class MachineACaféInterface(abc.ABC):
    @abc.abstractmethod
    def insérer(self, montant):
        pass