class Pièce:
    CinquanteCentimes = 50
    DeuxEuros = 200
    UnEuro = 100

    @staticmethod
    def valide(montant):
        return montant in [1, 5, 10, 20, Pièce.CinquanteCentimes, Pièce.UnEuro, Pièce.DeuxEuros]
