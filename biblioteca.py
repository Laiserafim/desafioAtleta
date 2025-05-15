
"""
Atleta - Aposentar() , Peso()
Corredor - correr()
Nadador - nadar()
Ciclista - pedalar()
TriAtleta()
"""


class Atleta():
    def __init__(self, aposentado, peso):
        self.aposentado = aposentado
        self.peso = peso

    def aposentar (self):
        print("Está aposentado")

    def peso (self):
        print(f"Está pesando {self.peso} kg")

class Corredor(Atleta):
    def __init__(self, aposentado,peso):
        super().__init__(aposentado,peso)

    def correr (self):
        print("O corredor corre")

class Nadador (Atleta):
    def __init__(self, aposentado, peso):
        super().__init__(aposentado,peso)

    def nadar(self):
        print(f"O nadador nada")

class Ciclista(Atleta):
    def __init__(self, aposentado, peso):
        super().__init__(aposentado, peso)

    def pedalar(self):
        print(f"O ciclista pedala")

class TriAtleta(Corredor, Nadador, Ciclista):
    def __init__(self, aposentado, peso):
        super().__init__(aposentado, peso)

