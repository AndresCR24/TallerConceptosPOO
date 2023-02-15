"""Cree una clase Circulo que tenga las propiedades centro y radio, las cuales se inicializan con parámetros en el constructor. Defina métodos en la clase para calcular 
el área, el perímetro e indicar si un punto pertenece al círculo o no."""
import math

class Circulo:

    def __init__(self, centro, radio):
        
        self.centro = centro
        self.radio = radio

    def area(self):
        area_circulo = round(math.pi*(self.radio**2),2)
        return area_circulo

    def primetro(self):
        
        perimetro_circulo = round(math.pi*(2*self.radio),2)
        return perimetro_circulo

