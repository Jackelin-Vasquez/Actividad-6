#Actividad no.6
def menu():
    print("1.Ingresar números y mostrar.")
    print("2.Calcular el área de un triángulo.")
    print("3.Vereficar si es un número par i impar.")
    print("4.Calcular el promedio de calificaciones")
    print("5.Ingresar n números y mostrar cual es mayor y menor")
    print("6.Salir del programa")

def opcion_uno():
        print("1.La suma total")
        print("2.El promedio")
        print("3.La cantidad de números positivos y negativos")

def opcion_dos(base,altura):
    return (base*altura)/2

def opcion_tres(numero):
    if numero % 2 ==0:
        print("Es par")
    else:
        print("es par")

def opcion_cuatro(suma,numeros):
    return suma/numeros


while True:
    menu()

    opcion= input("Ingrese una opcion:")



