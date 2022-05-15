# TIPOS DE DATOS

#  String
from xmlrpc.client import boolean


x = 'Palabra'
y = "Hola mundo con comilla doble"

# Números enteros
z = 20

# Números float
a = 2.102 #Con decimal

# Números complejos
b = 1j

# print(x, y, z, a, b)

# LISTA / LIST

#Así se declara una lista
listaVacia = []
lista = [1, 2, 3]

#Metodo para agregar un dato a la lista
lista.append(4)
#Método para copiar los mismos valores de lista en lista2
lista2 = lista.copy()
#Metodo para limpiar todos los datos de la lista
lista.clear()
#Método para saber cuantas veces se repite un dato
lista2.count(2)
#Método para saber el tamaño de lista
len(lista2)
#Acceder a los datos de una lista
lista2[0] # --> esto se hace con corchetes [] y dentro el índice del elemento que se desea acceder [2]
#Eliminar elementos de una lista
lista2.pop() # --> Elimina el último elemento de la lista
lista2.remove(2) # --> Elimina el valor que se ponga dentro de los parentesis 

#Método para revertir el orden de los valores dentro de la lista
lista2.reverse()
#Método para ordenar una lista
lista2.sort() #--> Solo se pueden ordenar listas con el mismo tipo de dato

# TUPLAS 
# A diferencia de las listas una vez creadas no podras cambiarlas (inmutables)

#Así se declara una tupla
tupla = ('Hola', 'como estas', 'bien')
#Método que te devuelve el indice del valor indicado entre parentesis
tupla.index('Hola')
#Método para caster de tupla a lista
lista3 = list(tupla)

# RANGOS

#Así se declara un rango
rango = range(6)

# DICCIONARIOS 
#Así se declara un diccionario
dictionary = {} 

diccionario = {
    "nombre" : 'Georgie',
    "raza" : 'Persa',
    "edad": 3,
}

#Acceder a un valor del diccionario
nombre = diccionario['nombre'] 
nombre = diccionario.get('nombre')

#Cambiar valores de un diccionario
diccionario['nombre'] = 'Pancracio'

#Obtener la longitud del diccionario
len(diccionario)

#Agregar valores a un diccionario
diccionario['ronronea'] = True
#Eliminar valores de un diccionario
diccionario.pop('ronronea')
diccionario.popitem() # --> Eliminara el último valor agregado al diccionario
del diccionario['ronronea']
#Generar copias de diccionario
copiaDiccionario = diccionario.copy()
copiaDiccionario2 = dict(diccionario)
#Eliminar todos los valores del diccionario
diccionario.clear()

#Diccionarios anidados

gatos = {
    'Georgie': {
        'nombre': 'Georgie',
        'edad': 3,
    },
    'Benito': {
        'nombre': 'Benito',
        'edad': 2
    } 
}

#Constructor Dict
perritos = dict(
    nombre= "Mosha",
    edad = 4
) 

# Booleanos
Verdadero = True
Falso = False 
 



