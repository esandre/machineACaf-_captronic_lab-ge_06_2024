import random
import unittest

from machine_a_café import MachineACafé
from pièce import Pièce


class ServiceTest(unittest.TestCase):
    def test_n_cafés(self):
        cas = [1, 2, random.Random().randint(3, 100)]

        for nombre_cafés_servis in cas:
            with self.subTest(nombre_cafés_servis):
                # ETANT DONNE une machine à café
                machine = MachineACafé()
                somme_initiale = machine.somme_encaissée_en_centimes
                nombre_cafés_initiaux = machine.nombre_cafés_servis

                # QUAND on insère 1€, <n> fois
                for n in range(nombre_cafés_servis):
                    machine.insérer(Pièce.UnEuro)

                # ALORS l'ordre de couler un café est envoyé 2 fois
                self.assertEqual(nombre_cafés_servis , machine.nombre_cafés_servis - nombre_cafés_initiaux)

                # ET le monnayeur contient l'argent en double
                self.assertEqual(100 * nombre_cafés_servis, machine.somme_encaissée_en_centimes - somme_initiale)


if __name__ == '__main__':
    unittest.main()
