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

    def depositar(self):
        
        ingresar_dinero = float(input("Ingrese la cantidad de dinero que desea deósitar: $"))
        ingrese_cuenta = int(input("Ingrese el numero de cuenta de la persona a la que desea depositar el dinero: "))
        ingrese_dinero = ingresar_dinero + self.balance
        self.control = ingresar_dinero + self.balance
        self.numero_cuenta = ingrese_cuenta
        
        return(f"El numero de cuenta es: {ingrese_cuenta}, El nombre del propietario es: {self.propietarios}, y el dinero que tiene en la cuenta es de: {ingresar_dinero}")

    def retirar(self):

        retirar_dinero = float(input("Ingrese la cantidad de dinero que desea retirar: $"))
        contraseña = int(input("Ingrese la contraseña: "))
        retiro = self.control - retirar_dinero
        self.balance = retiro

        return(f"El retiro fue exitoso quedas con este dinero disponible {retiro} la cuenta ")

    def aplicar_cuota_manejo(self):

        cuota_manejo = self.balance +(self.balance * 0.02)
        return(f"El valor con el 2% de cuota de manejo es de: {cuota_manejo}")

    def mostrar_detalles(self):
        return(f"El numero de cuenta es: {self.numero_cuenta} \n El nombre del titular de la cuenta es: {self.propietarios} \n El dinero que hay disponible en la cuenta es {self.balance}")


usuario_1 = CuentaBancaria(101, "Andres", 1000)
print(usuario_1.depositar())
print("-------------------------------------------------------------")
print(usuario_1.retirar())
print("-------------------------------------------------------------")
print(usuario_1.mostrar_detalles())
print("-------------------------------------------------------------")
print(usuario_1.aplicar_cuota_manejo())
