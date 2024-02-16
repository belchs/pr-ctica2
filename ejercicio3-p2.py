
def ingresar_datos():
    try:
        dato1 = float(input("Ingrese el primer dato: "))
        dato2 = float(input("Ingrese el segundo dato: "))
        return dato1, dato2
    except ValueError:
        print("Error: Ingrese datos válidos.")
        return ingresar_datos()

def division_entre_cero(dato1, dato2):
    try:
        resultado = dato1 / dato2
        print("La división es: {}".format(resultado))
    except ZeroDivisionError:
        print("Error: División entre cero.")

        dato2 = float(input("Ingrese un segundo dato diferente de cero: "))
        division_entre_cero(dato1, dato2)

def evaluar_suma(dato1, dato2):
    try:
        resultado = dato1 + dato2
        print("La suma es: {}".format(resultado))
    except TypeError:
        print("Error: La suma no pudo ser evaluada correctamente.")
        dato1n, dato2n = ingresar_datos()
        evaluar_suma(dato1n, dato2n)

num1, num2 = ingresar_datos()
division_entre_cero(num1, num2)
evaluar_suma(num1, num2)