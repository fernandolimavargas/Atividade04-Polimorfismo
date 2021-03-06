from Veiculo import Veiculo

class Bicicleta(Veiculo):
    def __init__(self, marca, qtdRodas, modelo, numMarchas, bagageiro):
        super().__init__(marca, qtdRodas, modelo)
        self.numMarchas = int(numMarchas)
        self.bagageiro = bagageiro

    def imprimirInformacoes(self):
        super().imprimirInformacoes()
        print(f"Numero de marchas: {self.numMarchas}")
        print(f"Bagageiro: {(self.bagageiro)}")