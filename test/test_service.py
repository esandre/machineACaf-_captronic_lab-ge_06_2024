import unittest

from machine_a_café import MachineACafé
from pièce import Pièce


class MyTestCase(unittest.TestCase):
    def test_cas_nominal(self):
        # ETANT DONNE une machine à café
        machine = MachineACafé()
        somme_initiale = machine.somme_encaissée_en_centimes
        nombre_cafés_initiaux = machine.nombre_cafés_servis

        # QUAND on insère 1€
        machine.insérer(Pièce.UnEuro)

        # ALORS l'ordre de couler un café est envoyé
        self.assertEqual(1, machine.nombre_cafés_servis - nombre_cafés_initiaux)

        # ET le monnayeur contient l'argent
        self.assertEqual(100, machine.somme_encaissée_en_centimes - somme_initiale)

    def test_2_cafés(self):
        # ETANT DONNE une machine à café
        machine = MachineACafé()
        somme_initiale = machine.somme_encaissée_en_centimes
        nombre_cafés_initiaux = machine.nombre_cafés_servis

        # QUAND on insère 1€, deux fois
        machine.insérer(Pièce.UnEuro)
        machine.insérer(Pièce.UnEuro)

        # ALORS l'ordre de couler un café est envoyé 2 fois
        self.assertEqual(2, machine.nombre_cafés_servis - nombre_cafés_initiaux)

        # ET le monnayeur contient l'argent en double
        self.assertEqual(200, machine.somme_encaissée_en_centimes - somme_initiale)


if __name__ == '__main__':
    unittest.main()
