from pièce import Pièce
from utilities.fake_lecteur_cb import OrdreDébit
from utilities.machine_a_cafe_matchers import MachineACaféMatchers
from utilities.machine_a_café_builder import MachineACaféBuilder


class TestRecette20240604(MachineACaféMatchers):
    def test_recette(self):
        machine = MachineACaféBuilder().ayant_un_lecteur_cb().build()

        machine.insérer(Pièce.CinquanteCentimes)
        machine.insérer(Pièce.UnEuro)
        machine.simuler_présentation_carte(True)
        machine.insérer(Pièce.DeuxEuros)
        machine.simuler_présentation_carte(False)

        self.assertNombreCafésServis(3, machine)
        self.assertSommeEncaissée(300, machine)

        ordres_debit = machine.get_ordres_débit()
        self.assertIn(OrdreDébit(70, True), ordres_debit)
        self.assertIn(OrdreDébit(70, False), ordres_debit)