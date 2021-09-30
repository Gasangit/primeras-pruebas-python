class Galleta:
    chocolate = False

    def __init__(self, sabor, color):
        self.sabor = sabor
        self.color = color
        print(f"Se acaba de crear una galleta {self.color} y {self.sabor}.")

galleta_1 = Galleta("marrón", "amarga")
galleta_2 = Galleta("blanca", "dulce")