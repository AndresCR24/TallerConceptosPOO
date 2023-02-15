"""Cree una clase CuentaBancaria que contenga los siguientes atributos: numero_cuenta, propietarios y balance. 
Los tres atributos se deben inicializar en el constructor con valores recibidos como parámetros.
Para la clase CuentaBancaria, cree un método depositar que maneje las acciones de depósito en la cuenta.
Para la clase CuentaBancaria, cree un método retirar que maneje las acciones de retiro de la cuenta.
Para la clase CuentaBancaria, cree un método aplicar_cuota_manejo que aplique un porcentaje del 2% sobre el balance de la cuenta
Para la clase CuentaBancaria, cree un método mostrar_detalles que imprima por consola los detalles de la cuenta bancaria."""

class CuentaBancaria:

    def __init__(self, numero_cuenta, propietarios, balance):

        self.numero_cuenta = numero_cuenta
        self.propietarios = propietarios
        self.balance = balance
        #self.control = 0

    def depositar(self, ingresar_dinero, ingrese_cuenta):
        
        ingresar_dinero = ingresar_dinero
        ingrese_cuenta = ingrese_cuenta
        self.balance += ingresar_dinero
        #self.control = ingresar_dinero + self.balance
        self.numero_cuenta = ingrese_cuenta
        
        return self.numero_cuenta, self.balance

    def retirar(self, retirar_dinero):

        retirar_dinero = retirar_dinero
        self.balance -= retirar_dinero

        return self.balance

    def aplicar_cuota_manejo(self):

        cuota_manejo = self.balance +(self.balance * 0.02)
        self.balance = cuota_manejo
        return self.balance

    def mostrar_detalles(self):
        return self.numero_cuenta, self.propietarios, self.balance

#Prueba del funcionamiento del codigo
usuario_1 = CuentaBancaria(101, "Andres", 1000)
print(usuario_1.depositar(2000, 104))
print("-------------------------------------------------------------")
print(usuario_1.retirar(1000))
print("-------------------------------------------------------------")
print(usuario_1.mostrar_detalles())
print("-------------------------------------------------------------")
print(usuario_1.aplicar_cuota_manejo())
print("--------------------------------------------------------------")
print(usuario_1.mostrar_detalles())