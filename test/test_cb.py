from utilities.machine_a_cafe_matchers import MachineACaféMatchers
from utilities.machine_a_café_builder import MachineACaféBuilder


class ServiceTest(MachineACaféMatchers):
    def test_cas_nominal(self):
        # ETANT DONNE une machine à café munie d'un lecteur CB
        machine = MachineACaféBuilder().ayant_un_lecteur_cb().build()

        # ET une carte solvable
        # QUAND on présente cette carte
        machine.simuler_présentation_carte(solvable=True)

        # ALORS l'ordre de couler un café est envoyé
        self.assertNombreCafésServis(1, machine)

        # ET un ordre de débit est validé pour 70cts
        ordre_débit = machine.get_ordres_débit()[0]

        montant = 70
        self.assertEqual(montant, ordre_débit.montant_en_centimes)
        self.assertTrue(ordre_débit.validé)

    def test_insolvable(self):
        # ETANT DONNE une machine à café munie d'un lecteur CB
        machine = MachineACaféBuilder().ayant_un_lecteur_cb().build()

        # QUAND on présente cette carte
        machine.simuler_présentation_carte(solvable=False)

        # ALORS l'ordre de couler un café n'est pas envoyé
        self.assertNombreCafésServis(0, machine)
