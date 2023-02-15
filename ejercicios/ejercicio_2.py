# 2. Cree una clase Punto que represente un punto en el plano cartesiano.
""" 3. A la clase del punto anterior, defínale los siguientes métodos:
- Un método mostrar que imprima por consola las coordenadas del punto
- Un método mover que cambie las coordenadas del punto"""
import math

class Punto:

    def __init__(self,valor_ejex:int, valor_ejey:int):
        
        self.valor_ejex:int = valor_ejex
        self.valor_ejey:int = valor_ejey

    def mostrar(self):

        print(f"Las cordenas ingresadas son ({self.valor_ejex},{self.valor_ejey})")
    
    def cambiar_puntos(self):

        self.valor_ejex = int(input("Ingrese el nuevo valor de la coordenada en el eje X: "))
        self.valor_ejey = int(input("Ingrese el nuevo valor de la coordenada en el eje Y: "))

    def mover(self):
        desplazamiento_x = int(input("Ingrese lo que desea desplazar en X la coordenada: "))
        desplazamiento_y = int(input("Ingrese lo que desea desplazar en Y la cordenada: "))
        self.valor_ejex += desplazamiento_x
        self.valor_ejey += desplazamiento_y
    
    def distancia(self, punto2):

        cateto_1 = punto2.valor_ejey - self.valor_ejey
        cateto_2 = punto2.valor_ejex - self.valor_ejex
        d = math.sqrt((cateto_1**2) + (cateto_2**2))
        return (f"La distancia entre los puntos es de {d}")
        
