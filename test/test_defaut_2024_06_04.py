from utilities.machine_a_cafe_matchers import MachineACaféMatchers
from utilities.machine_a_café_builder import MachineACaféBuilder


class TestDéfaut2024_06_04(MachineACaféMatchers):
    # Il a été possible d'introduire une fausse pièce de 1€05
    # Le café a coulé

    def test_enquete(self):
        # ETANT DONNE une somme ne correspondant pas à une valeur de pièce en euro valide
        cas = [0, 3, 4, 6, 9, 11, 19, 21, 49, 51, 99, 101, 199, 201]

        for montant in cas:
            with self.subTest(montant):
                # ET une machine a café
                machine_a_café = MachineACaféBuilder().par_defaut()

                # QUAND on insère cette pièce
                action = lambda: machine_a_café.insérer(montant)

                # ALORS une exception est lancée
                self.assertRaises(Exception, action)
