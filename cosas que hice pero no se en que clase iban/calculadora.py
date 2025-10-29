menu =  "Opción 1: Suma\n" \
        "Opción 2: Resta\n" \
        "Opción 3: Producto\n" \
        "Opción 4: Cociente"


print(menu)
opcion = int(input("Ingrese una opción del 1 al 4: "))


while opcion < 5:

    match opcion:
        case 1:
            opcion_suma = ""
            resultado_suma = 0
            valores_suma = []
            contador = 0

            while opcion_suma != "=":
                contador += 1
                valor = int(input(f"Ingrese el valor {contador}: "))
                valores_suma.append(valor)
                opcion_suma = input("ingrese = para mostrar resultado, enter para seguir introduciendo valores: ")
                if opcion_suma == "=":
                    for i in valores_suma:
                        resultado_suma = resultado_suma + i
            print(f"\nEl resultado de la suma es: {resultado_suma}\n")
        case 2:
            opcion_resta = ""
            resultado_resta = 0
            valores_resta = []
            contador = 0

            while opcion_resta != "=":
                contador += 1
                valor = int(input(f"Ingrese el valor {contador}: "))
                valores_resta.append(valor)
                opcion_resta = input("ingrese = para mostrar resultado, enter para seguir introduciendo valores: ")
                if opcion_resta == "=":
                    for i in range(len(valores_resta)-1):
                        resultado_resta = resultado_resta + (valores_resta[i] - valores_resta[i+1])
                        print(resultado_resta)
                print(f"El resultado de la resta es: {resultado_resta}")
        case 3:
            opcion_producto = ""
            resultado_producto = 1
            valores_producto = []
            contador = 0

            while opcion_producto != "=":
                contador += 1
                valor = int(input(f"Ingrese el valor {contador}: "))
                valores_producto.append(valor)
                opcion_producto = input("ingrese = para mostrar resultado, enter para seguir introduciendo valores: ")
                if opcion_producto == "=":
                    for i in valores_producto:
                        resultado_producto = resultado_producto * i
                        print(resultado_producto)
                print(f"El resultado del producto es: {resultado_producto}")
        case 4:
            opcion_cociente = ""
            resultado_cociente = 0
            valores_cociente = []
            contador = 0

            while opcion_cociente != "=":
                contador += 1
                valor = int(input(f"Ingrese el valor {contador}: "))
                valores_cociente.append(valor)
                opcion_cociente = input("ingrese = para mostrar resultado, enter para seguir introduciendo valores: ")
                if opcion_cociente == "=":
                    for i in range(len(valores_cociente)-1):
                        resultado_cociente = resultado_cociente + (valores_cociente[i] // valores_cociente[i+1])
                    print(f"El resultado de la división entera es: {resultado_cociente}")

    
    opcion = int(input("Ingrese una opción del 1 al 4: "))