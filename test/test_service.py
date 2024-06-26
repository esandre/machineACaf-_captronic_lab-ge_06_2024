import itertools
import random
import unittest

from pièce import Pièce
from functools import reduce
from operator import add

from utilities.machine_a_cafe_matchers import MachineACaféMatchers
from utilities.machine_a_café_builder import MachineACaféBuilder


class ServiceTest(MachineACaféMatchers):

    def test_defaillante(self):
        # ETANT DONNE une machine à café
        machine = (MachineACaféBuilder()
                   .défaillante()
                   .build())
        somme_initiale = machine.get_somme_encaissée_en_centimes()

        # QUAND on insère une somme supérieure ou égale à 1€
        machine.insérer(Pièce.UnEuro)

        # ALORS l'argent est rendu
        self.assertEqual(0, machine.get_somme_encaissée_en_centimes() - somme_initiale)

    def test_pas_assez_argent(self):
        # ETANT DONNE une machine à café
        machine = MachineACaféBuilder.par_defaut()

        # QUAND on insère une somme inférieure à 1€
        machine.insérer(Pièce.CinquanteCentimes)

        # ALORS l'ordre de couler un café n'est pas envoyé
        self.assertNombreCafésServis(0, machine)

        # ET l'argent est rendu
        self.assertAucuneSommeEncaissée(machine)

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
                machine = MachineACaféBuilder.par_defaut()

                # QUAND on insère une somme supérieure ou égale à 1€, <n> fois
                for pièce in pièces_a_insérer:
                    machine.insérer(pièce)

                # ALORS l'ordre de couler un café est envoyé <n> fois
                nombre_cafés_servis = len(pièces_a_insérer)
                self.assertNombreCafésServis(nombre_cafés_servis, machine)

                # ET le monnayeur contient l'argent
                somme_totale = reduce(add, pièces_a_insérer)
                self.assertSommeEncaissée(somme_totale, machine)


if __name__ == '__main__':
    unittest.main()
