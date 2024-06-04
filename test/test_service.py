import itertools
import random
import unittest

from machine_a_café import MachineACafé
from pièce import Pièce
from functools import reduce
from operator import add


class ServiceTest(unittest.TestCase):
    def test_n_cafés(self):
        cas = [
            [Pièce.UnEuro],
            [Pièce.DeuxEuros],
            [Pièce.UnEuro, Pièce.UnEuro],
            list(itertools.repeat(Pièce.UnEuro, random.Random().randint(3, 20)))
        ]

        for pièces_a_insérer in cas:
            with self.subTest(pièces_a_insérer):
                # ETANT DONNE une machine à café
                machine = MachineACafé()
                somme_initiale = machine.somme_encaissée_en_centimes
                nombre_cafés_initiaux = machine.nombre_cafés_servis

                # QUAND on insère une somme supérieure ou égale à 1€, <n> fois
                for pièce in pièces_a_insérer:
                    machine.insérer(pièce)

                # ALORS l'ordre de couler un café est envoyé <n> fois
                nombre_cafés_servis = len(pièces_a_insérer)
                self.assertEqual(nombre_cafés_servis , machine.nombre_cafés_servis - nombre_cafés_initiaux)

                # ET le monnayeur contient l'argent
                somme_totale = reduce(add, pièces_a_insérer)
                self.assertEqual(somme_totale, machine.somme_encaissée_en_centimes - somme_initiale)


if __name__ == '__main__':
    unittest.main()
