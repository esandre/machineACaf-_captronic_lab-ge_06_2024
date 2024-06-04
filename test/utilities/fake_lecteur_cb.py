from typing import Callable

from lecteur_cb_interface import LecteurCbInterface, CarteDétectée


class FakeLecteurCb(LecteurCbInterface):
    def __init__(self):
        self.__ordres_debit = []
        self.__callback: Callable[[CarteDétectée], None] = None

    def register(self, callback: Callable[[CarteDétectée], None]):
        self.__callback = callback

    def simuler_présentation_carte(self, solvable):
        self.__callback(FakeCarteDétectée(self.__ordres_debit, solvable))

    def get_ordres_debit(self):
        return self.__ordres_debit


class FakeCarteDétectée(CarteDétectée):
    def __init__(self, ordres, solvable):
        self.__solvable = solvable
        self.__ordres = ordres

    def tenter_debit(self, somme):
        self.__ordres.append(OrdreDébit(somme, self.__solvable))
        return self.__solvable


class OrdreDébit:
    def __init__(self, montant_en_centimes, validé):
        self.montant_en_centimes = montant_en_centimes
        self.validé = validé

    def __str__(self):
        return f"Validé:{self.validé} pour {self.montant_en_centimes}cts"
