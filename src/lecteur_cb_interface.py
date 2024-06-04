import abc
from typing import Callable


class CarteDétectée(abc.ABC):
    @abc.abstractmethod
    def tenter_debit(self, somme) -> bool:
        pass


class LecteurCbInterface(abc.ABC):
    @abc.abstractmethod
    def register(self, callback: Callable[[CarteDétectée], None]):
        pass


class AucunLecteurCb(LecteurCbInterface):
    def register(self, callback: CarteDétectée):
        pass
