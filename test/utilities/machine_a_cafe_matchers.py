import unittest

from utilities.hardware_pouvant_etre_surveillé import HardwareSpy


class MachineACaféMatchers(unittest.TestCase):
    def assertNombreCafésServis(self, attendu, hardware: HardwareSpy):
        self.assertEqual(attendu, hardware.nombre_appels_a_couler_un_café())