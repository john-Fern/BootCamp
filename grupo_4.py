# Contador de numeros pares e impares
contador_pares = 0
contador_impares = 0
 
# Recorrer los números del 1 al 10
for numero in range(1, 11):
    if numero % 2 == 0:
        print(f"{numero} - Número par")
        contador_pares += 1  
    else:
        print(f"{numero} - Número impar")
        contador_impares += 1
 
# Mensaje final
print("Proceso completado")
 
# Mostrar totales
print(f"Total pares: {contador_pares}")
print(f"Total impares: {contador_impares}")