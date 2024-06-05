from typing import Callable

from lecteur_cb_interface import LecteurCbInterface, CarteDétectée


class LecteurCbAdapter(LecteurCbInterface):
    def register(self, callback: Callable[[CarteDétectée], None]):
        raise Exception()

