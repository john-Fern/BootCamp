# Asignación
numero_entero = 5
numero_float = 2.5

# # Comparación
# if numero_entero > 0:
#     print(f"El número es {numero_entero}")

# While es mientras

# contador = 1

# while contador < 6:
#     print(contador)
#     contador+= 1

# for i in range(1,6):
#     print("Número:",i)

# for i in range(0,10):
#     print("Número",i)

for i in range(1,16):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)