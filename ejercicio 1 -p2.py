from datetime import datetime, date

class Persona:
    def __init__(self, nombre, edad, saldo) :
        self.nombre = nombre
        self.edad = self.edad_val(edad)
        self.saldo = saldo
        self.nacionalidad = "peruana"

    def edad_val(self, edad):
        try:
            return int(edad)
        except ValueError:
            print("Error: La edad debe ser un número entero.")
            return None
    def solicitar_nombre_y_edad(self):
        self.nombre = input("Ingrese su nombre: ")
        nueva_edad = input("Ingrese su edad: ")
        self.edad = self.edad_val(nueva_edad)



