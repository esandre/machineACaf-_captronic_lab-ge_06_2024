import abc


class CarteDetecteeCallback(abc.ABC):
    @abc.abstractmethod
    def tenter_debit(self, somme):
        pass


class LecteurCbInterface(abc.ABC):
    @abc.abstractmethod
    def register(self, callback: CarteDetecteeCallback):
        pass