import unittest

from utilities.hardware_spy import HardwareSpy
from utilities.machine_a_café_harness import MachineACaféHarness


class MachineACaféMatchers(unittest.TestCase):
    def assertNombreCafésServis(self, attendu, machine: MachineACaféHarness):
        self.assertEqual(attendu, machine.nombre_appels_a_couler_un_café())

    def assertAucuneSommeEncaissée(self, machine: MachineACaféHarness):
        self.assertSommeEncaissée(0, machine)

    def assertSommeEncaissée(self, somme, machine: MachineACaféHarness):
        self.assertEqual(somme, machine.get_delta_argent_encaissé())