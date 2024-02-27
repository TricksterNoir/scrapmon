class Calculo():
    def __init__(self, numero):
        self.numero = numero

    def converte_polegada(self):
        feats, pol = self.numero.split("'")
        pol = pol.strip("\n")
        pol = pol.strip('"')

        feats = float(feats) * 30.48
        pol = float(pol) * 2.54

        return f'{round((feats + pol)/100,2)}m'