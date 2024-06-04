import unittest

from machine_a_café import MachineACafé
from pièce import Pièce


class MyTestCase(unittest.TestCase):
    def test_cas_nominal(self):
        # ETANT DONNE une machine à café
        machine = MachineACafé()

        # QUAND on insère 1€
        machine.insérer(Pièce.UnEuro)

        # ALORS l'ordre de couler un café est envoyé
        self.assertEqual(1, machine.nombre_cafés_servis)

        # ET le monnayeur contient l'argent
        self.assertEqual(100, machine.somme_encaissée_en_centimes)


if __name__ == '__main__':
    unittest.main()
