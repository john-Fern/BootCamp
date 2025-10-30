# Clase 1 Python

### Imprimir un mensaje por consola
```python
print("Hola Mundo")
```

### Comentarios
- Comentario de línea
```python
# Este es un comentario de línea
```
- Comentario de bloque
```python
"""
Este es un comentario de bloque
donde puedo ir comentando
en varias lineas
"""
```

### Palabras reservadas
- Condicionales
```python
a = 2 # asigno un valor entero a mi variable a
b = 1 # asigno un valor entero a mi variable b
if a > b: # pregunto si a es mayor que b
    print(a) # en el caso de que a sea mayor que b, imprime por pantalla el valor de a
# todo lo que se escriba fuera o después del bloque if, se va a ejecutar sea la condición anterior verdadera o falsa
```
- Ciclos
```python
lista = [1,2,3,4,5] # asgino a mi lista 5 valores enteros

for elemento in lista # para cada elemento en mi lista
    print(elemento) # se imprimiran cada elemento por iteracion
```

### Convenciones
- snake_case
```python
variable_de_snake_case = "holaa" # guardo una cadena de caracteres en mi variable
```
- CamelCase
```python
VariableCamelCase = "chaito" # guardo una cadena de caracteres en mi variable
```
- UPPER_SNAKE_CASE
```python
VARIABLE_SNAKE_CASE = 3.14 # Asigno un valor decimal a mi variable
```

## Funciones
```python
def imprimir_nombre(): # Defino mi funcion 
    nombre = input("Introduzca su nombre") # Creo una variable y le asigno la función input, la cual pregunta un nombre por pantalla, y guarda el valor (string) que el usuario coloque. Si se pone un valor fuera de los strings va a arrojar error.
    print(nombre)
```

## Variables
- Números enteros
```python
numero_entero = 25 # Asigno número entero a mi variable
```
- Números décimales
```python
pi = 3.14159 # Asigno un número décimal (float) a mi variable
```
- Cadena de Caracteres
```python
# Asigno mi nombre y el curso en el que estoy a variables
nombre = "Jonathan"
curso = "Java"
```
- Booleanos
```python
falso = False
vacio = None

print(falso == None)
```

## Formas comunes de imprimir por pantalla
```python
print("1. simple") # Forma simple de escribir una cadena de caracteres
print(("2. Hola mundillo"))
print("3. hola", "mundo") # Concatena los valores y le pone un espacio entre las palabras
print("4. hola" + "mundo") # Contanera los valores sin poner espacio entre las palabras
print(f"5. hola {'mundo'}") # F-String permite poner variables, hacer operaciones matematicas, comprobar booleanos etc. dentro el print. Cosa que con la forma simple no se podría
print("6. Hola", "Chaito", sep="-") # Sep es un atributo que permite separar los valores por el caracter que se necesite para representar mejor el mensaje
print("7. Hola", "Como tas", end="?") # end es un atributo que pone un caracter al final del mensaje en pantalla

# Concatenar variable en un print
nombre = "Jony"
print("Hola", nombre)

print("\nHola %s, tienes %d anios\n" % (nombre, 30)) # imprimo una cadena de caracteres. El %s indica que primero irá una variable de tipo string y el %d indica que en ese espacio irá una variable en tipo entero. Esta es una forma tipica de imprimir en el lenguaje C

print("PI {:.2f}".format(3.14156)) # en este caso usamos format para imprimir solo 2 decimales del valor introducido dentro del parentesis(parametro de entrada) de format
```