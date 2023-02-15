#Cree una clase Vehículo que contenga los atributos de instancia velocidad_maxima y kilometraje.

class Vehiculo:
    
    def __init__(self, velocidad_maxima: float, kilometraje: float):
        
        self.velocidad_maxima: float = velocidad_maxima
        self.kilometraje: float = kilometraje


        