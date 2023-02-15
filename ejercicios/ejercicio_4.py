"""Cree una clase Rectángulo la cual contiene dos atributos de instancia que representan los puntos 
que definen sus esquinas. Agregue métodos a la clase Rectángulo para calcular su perímetro, calcular 
su área e indicar si el rectángulo es un cuadrado."""
import math

class Rectangulo:


    def __init__(self, coordenada_1, coordenada_2, coordenada_3, coordenada_4):

        self.coordenada_1 = coordenada_1
        self.coordenada_2 = coordenada_2
        self.coordenada_3 = coordenada_3
        self.coordenada_4 = coordenada_4

    def puntos(self,):

        #valor_ejex = 
        #valor_ejey = 
        #self.coordenada_1 =[valor_ejex,valor_ejey]
        pass


    def distancia(self, punto2):

        cateto_1 = punto2.valor_ejey - self.valor_ejey
        cateto_2 = punto2.valor_ejex - self.valor_ejex
        d = math.sqrt((cateto_1**2) + (cateto_2**2))
        return d

    def perimetro(self):
        pass

    def area(self):
        pass

    def es_cuadrado(self):
        pass

rectangulo_1 = Rectangulo(1, 2, 6, 3)
rectangulo_1.distancia()