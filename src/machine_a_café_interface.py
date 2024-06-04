import abc


class MachineACaféInterface(abc.ABC):
    @abc.abstractmethod
    def insérer(self, montant):
        pass

    @abc.abstractmethod
    def get_somme_encaissée_en_centimes(self):
        pass
