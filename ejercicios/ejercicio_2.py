#Cree una clase Punto que represente un punto en el plano cartesiano.
"""A la clase del punto anterior, defínale los siguientes métodos:
- Un método mostrar que imprima por consola las coordenadas del punto
- Un método mover que cambie las coordenadas del punto"""

class Punto:

    def __init__(self,valor_ejex, valor_ejey):
        
        self.valor_ejex = valor_ejex
        self.valor_ejey = valor_ejey

    def mostrar(self):

        print(f"Las cordenas ingresadas son ({self.valor_ejex},{self.valor_ejey})")
    
    def mover(self):

        self.valor_ejex = input("Ingrese el nuevo valor de la coordenada en el eje X: ")
        self.valor_ejey = input("Ingrese el nuevo valor de la coordenada en el eje Y: ")

punto_1 = Punto(2, 4)

punto_1.mostrar()
punto_1.mover()
punto_1.mostrar()