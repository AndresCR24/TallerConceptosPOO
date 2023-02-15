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

        return self.valor_ejex,self.valor_ejey
    
    def cambiar_puntos(self, nuevo_valor_x, nuevo_valor_y):

        self.valor_ejex = nuevo_valor_x
        self.valor_ejey = nuevo_valor_y
        return self.valor_ejex, self.valor_ejey


    def mover(self, desplazamiento_x, desplazamiento_y):
        desplazamiento_x = desplazamiento_x
        desplazamiento_y = desplazamiento_y
        self.valor_ejex += desplazamiento_x
        self.valor_ejey += desplazamiento_y
        return self.valor_ejex, self.valor_ejey
        
    
    def distancia(self, punto2):

        cateto_1 = punto2.valor_ejey - self.valor_ejey
        cateto_2 = punto2.valor_ejex - self.valor_ejex
        d = math.sqrt((cateto_1**2) + (cateto_2**2))
        return d


punto_1 = Punto(1,2)
punto_2 = Punto(6,2)

print(punto_1.distancia(punto_2))
print(punto_1.mostrar())
print(punto_1.mover(1,1))
print(punto_1.cambiar_puntos(0,0))