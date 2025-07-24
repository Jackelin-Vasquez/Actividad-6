#Actividad no.6

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

def opcion_cinco(cantidad):
    numero= int(input("Ingrese numero 1;"))
    mayor = numero
    menor = numero
    for i in range(1, cantidad):
        numero = int(input(f"Ingerse número {i+1}:"))
        if numero > mayor:
            mayor = numero
        if numero < menor:
            menor = numero
    return mayor, menor


while True:
    menu()

    opcion= input("Ingrese una opcion:")

    match opcion:
        case "1":
            resultados = pedir_numeros()
            while True:
                print("¿Que desea realizar?")
                menu2()

                sub_opcion= input("Ingrese una opcion:")

                match sub_opcion:
                    case "1":
                        print(f"La suma de los numeros es:{resultados[0]}")
                    case "2":
                        if resultados[0] > 0:
                            print(f"El promedio es:{promedio(resultados[0],resultados[1])}")
                        else:
                            print("No hay numeros ingresados")
                    case "3":
                        print(f"Hay {resultados[2]} positivos y {resultados[3]} negativos")
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

        case "4":
            suma=0
            numero_calificaciones= int(input("Ingrese cantidad de calificaciones:"))
            if numero_calificaciones < 0:
                print("Ingrese calificaciones")
            else:
                for i in range(numero_calificaciones):
                    calificacion= float(input(f"Ingrese calificacion {i+1}:"))
                    if calificacion < 0 or calificacion > 100:
                        print("Número no valido")
                    else:
                        suma += calificacion
                print(f"El promedio es {promedio(suma,numero_calificaciones)}")

        case "5":
            cantidad= int(input("Ingrese cantidad de números:"))
            if cantidad > 0:
                resultado= opcion_cinco(cantidad)
                mayor= resultado[0]
                menor= resultado[1]
                print(f"El numero mayor es {mayor} y el número menor es {menor}")
        case "6":
            print("Saliendo del programa:")
            break
        case _:
            print("Opcion no valida....")



