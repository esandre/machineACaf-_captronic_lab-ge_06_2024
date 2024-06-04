from typing import Callable

from lecteur_cb_interface import LecteurCbInterface, CarteDétectée


class FakeLecteurCb(LecteurCbInterface):
    __callback: Callable[[CarteDétectée], None] = None
    __ordres_debit = []
    
    def register(self, callback: Callable[[CarteDétectée], None]):
        self.__callback = callback

    def simuler_présentation_carte(self):
        self.__callback(FakeCarteDétectée(self.__ordres_debit))

    def get_ordres_debit(self):
        return self.__ordres_debit


class FakeCarteDétectée(CarteDétectée):
    def __init__(self, ordres):
        self.__ordres = ordres

    def tenter_debit(self, somme):
        self.__ordres.append(OrdreDébit(somme, True))


class OrdreDébit:
    def __init__(self, montant_en_centimes, validé):
        self.montant_en_centimes = montant_en_centimes
        self.validé = validé
