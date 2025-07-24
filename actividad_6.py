#Actividad no.6
suma= 0

def menu():
    print("1.Ingresar números y mostrar.")
    print("2.Calcular el área de un triángulo.")
    print("3.Vereficar si es un número par i impar.")
    print("4.Calcular el promedio de calificaciones")
    print("5.Ingresar n números y mostrar cual es mayor y menor")
    print("6.Salir del programa")

def menu2():
    print("1.La suma total\n 2.Promedio.\n 3.la cantidad de números positivos y negativos.\n 4. Salir")

def pedir_numeros():
    cantidad= int(input("Ingrese la cantidad de números que desea:"))

    suma= 0
    contador=0
    positivo=0
    negativo=0

    for i in range(cantidad):
        numero=int(input("Ingrese número a agregar:"))
        suma += numero
        contador+= 1

        if numero > 0:
            positivo += 1
        else:
            negativo +=1
    return suma, contador,positivo,negativo

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
        print("es impar")

def promedio(suma,numeros):
    return suma/numeros


while True:
    menu()

    opcion= input("Ingrese una opcion:")

    match opcion:
        case "1":
            suma, contador, positivo, negativo = pedir_numeros()
            while True:
                print("¿Que desea realizar?")
                menu2()

                sub_opcion= input("Ingrese una opcion:")

                match sub_opcion:
                    case "1":
                        print(f"La suma de los numeros es:{suma}")
                    case "2":
                        if contador > 0:
                            print(f"El promedio es:{promedio(suma,contador)}")
                        else:
                            print("No hay numeros ingresados")
                    case "3":
                        print(f"Hay {positivo} positivos y {negativo} negativos")
                    case "4":
                        print("Saliendo de opciones...")
                        break
        case "2":
            base= float(input("Ingrese la longitud de la base:"))
            altura= float(input("Ingrese altura:"))
            print(f"El ares del triangulo es:{opcion_dos(base,altura)}")

        case "3":
            numero= int(input("Ingrese número entero:"))
            opcion_tres(numero)




