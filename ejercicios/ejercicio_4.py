"""Cree una clase Rectángulo la cual contiene dos atributos de instancia que representan los puntos 
que definen sus esquinas. Agregue métodos a la clase Rectángulo para calcular su perímetro, calcular 
su área e indicar si el rectángulo es un cuadrado."""
import math

from ejercicio_2 import Punto

class Rectangulo:


    def __init__(self, punto_1: Punto, punto_2: Punto):
        
        self.punto_1 = punto_1
        self.punto_2 = punto_2

    def perimetro(self):
        
        return (self.ancho() + self.alto()) * 2

    def ancho(self):

        return abs(self.punto_2.valor_ejex - self.punto_1.valor_ejex)

    def alto(self):
        return abs(self.punto_2.valor_ejey - self.punto_1.valor_ejey)

    def area(self):
        
        return self.ancho() * self.alto()

    def es_cuadrado(self):

        return self.ancho() == self.alto()