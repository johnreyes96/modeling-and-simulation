# Asignamos el valor 3 a una variable que creamos, de nombre x
x = 3

# Evaluamos e imprimimos en pantalla el resultado
print(x)

# Asignamos el valor 15.7 a una nueva variable, de nombre y
y = 15.7

print(y)

# Podemos definir una nueva variable como la suma de dos anteriores
z = x + y

print(z)

# Se peude tambier asignar un valor de texto otra variable
un_texto = 'HOLA!'

print(un_texto)

print(un_texto)
print("un_texto")

# Si queremos, podemos borrar alguna variable que ya no utilizaremos más
del un_texto
# print(un_texto)

a = 42
print(type(a))

b = 7.8
print(type(b))

c = True
print(type(c))

t1 = 'hola'
print(type("hola"))

t2 = '523'
print(type('t2'))

# Este es un tipo especial de variable, que se utiliza para simbolizar algo 'vacio'
d = None
print(type(d))

numero = 45
print(type(numero))

# Quiero que sea un 'float' y no un int
numero = float(45)
print(type(numero))

# Quiero que sea un 'string' y no un int
numero = str(45)
print(type(numero))

otro_numero = 45.0
print(type(otro_numero))

# Quiero que sea un 'int' y no un 'float'
otro_numero = int(45.0)
print(type(otro_numero))

numero = '5'
numero = float(numero)

# Ejercicio: Cambiar el tipo de la variable 'numero' a float.
# La siguientes lineas de codigo chequean si hiciste correctamente el ejercicio
# No importa si no entiendes qué hace.
if type(numero) is float:
    print('Correcto!')
else:
    print('Convierte la variable a tipo float')

a = 20
b = 4
print(a+b)
print(a-b)

a = 20
b = 4.5

c = a+b
d = a-b

print(c)
print(d)

a = 20
b = 4.5

c = a+b
d = a-b

print(c)
print(d)

print(type(c))
print(type(d))

x = 10
y = 3
z = x/y
print(z)

print(type(z))

x = 10
y = 3
print(x%y)
print(type(x%y))

# Ejercicio: Calcular el porcentaje que representa el valor 17 sobre un total de 54 y guardarlo en una variable llamada
# porcentaje.
# COMPLETAR
porcentaje = 17/54*100
print(porcentaje)

# Ejercicio: calcula la suma y multiplicación de las variables a, b y c.
a = '2'
b = '-5.5'
c = '7.8'

# COMPLETAR
suma = a + b + c
print(suma)

lista_1 = [42, 10.7, True, 'Texto']
print(lista_1)

len(lista_1)

lista_2 = [5, 6.0,'Un poco de texto',-5, False, 'Más texto', True, 100]

print(lista_2[0])
print(lista_2[1])
print(lista_2[2])

lista_2 = [5, 6.0,'Un poco de texto',-5, False, 'Más texto', True, 100]
# COMPLETAR
print(lista_2[6])

lista_2 = [5, 6.0,'Un poco de texto',-5, False, 'Más texto', True, 100]
print(lista_2[0:4])
print(lista_2[4:])
print(lista_2[0:8:3])

lista_2 = [5, 6.0,'Un poco de texto',-5, False, 'Más texto', True, 100]
print(lista_2[-1])
print(lista_2[-2])
print(lista_2[-8])

# Definimos una segunda lista
lista_3 = [0, lista_1, 'Mas texto', lista_2]
print(lista_3)
print(len(lista_3))

print(lista_3[3])

# Ejercicio: tomando lista_1 desde lista_3 (lo que acabamos de hacer en la celda anterior), indexar el tercer elemento
# de lista_1. Debería darte como resultado True.
# COMPLETAR
lista_3 = [0, lista_1, 'Mas texto', lista_2]
#print(lista_3[1][2])
print(lista_3)
print(lista_3[3][4])

lista_vacia = []
len(lista_vacia)

lista_vacia.append(42)
lista_vacia.append('un segundo item')
print(lista_vacia)
print(len(lista_vacia))

# Ejercicio: Defina una lista vacia llamada lista_nueva y agréguele (append()) los elementos a, b y c.
a = 8
b = 'world'
c = [12,24.5,66]

lista_nueva = []
lista_nueva.append(a)
lista_nueva.append(b)
lista_nueva.append(c)
# COMPLETAR
print(lista_nueva)

lista_1 = [1,2,3,4]
lista_2 = lista_1  # lista_2 ahora es igual a lista_1
lista_2[-1] = 100 # el ultimo elemento de la lista_2 ahora es 100
print(lista_1, lista_2)

lista_numeros = [3,55,1,876,12]
for elemento in lista_numeros:
    # Definimos el codigo dentro del for mediante la indentación
    # (Todo lo que este corrido un 'tab' a la derecha)
    print(elemento)
print(elemento)

lista_numeros = [3,55,1,876,12]
i = 0 # La iniciamos en cero

for elemento in lista_numeros:
    i = i+1 # Le sumamos 1 cada vez que entra
    print(elemento, i)

lista_nombres = ['Ernesto', 'Camilo', 'Violeta']
nueva_lista = []

for item in lista_nombres:
    oracion = 'Mi nombre es ' + item
    nueva_lista.append(oracion)

# Este print esta fuera del bucle, no está indentado
print(nueva_lista)
print(len(nueva_lista))

numeros = [0,1,2,3,4,5,6,7,8,9]
# print(numeros + 3)

# COMPLETAR 1
for number in numeros:
  print(number + 3)

# COMPLETAR 2
new_list = []
for number in numeros:
  new_list.append(number + 3)

print(new_list)

# Ejercicio 3: Genere una lista llamada numerosgrandes que contenga el cuadrado de cada elemento en la lista numeritos.
numeritos = [3,1,5,7,12,10,17,4,22]
# COMPLETAR
numerosgrandes = []
for number in numeritos:
  numerosgrandes.append(number ** 2)

print(numerosgrandes)

# Ejercicio 4: qué ocurre si sumas,+, dos listas. ¿Cómo se llama esa operación?
lista_1 = [1,5,-8,3]
lista_2 = [True, 'Cocodrilo que se duerme es cartera', 9, -17, 98, False]
# COMPLETAR
print(lista_1 + lista_2)

# Ejercicio 5: sumar todos los elementos de la siguiente lista.
numeros = [4,8,3,1,-3,3,-5,1,2,-8]
# COMPLETAR
suma = 0
for number in numeros:
  suma = suma + number

print(suma)
