# Una tupla se usa cuando sabemos que no se modificaran los datos contenidos.
# Una tupla no permite modificar valores.


x = (1,2,3,3,5,6,7,3)
print type(x)
print x[2]
print x[2:5]
# Devuelve la posicion del elemento a buscar
print x.index(3)
# Cuenta cuantos elementos hay repetidos en la tupla
print x.count(3)
# Se pueden establecer listas dentro de las tuplas.
li = (['a','b','c'],[1,2,3,4,5])
print li

# Asigna valores a una tupla y no es necesarios los parentesis
a = 1,2,3
print a
print type(a)

# Python reconoce como tupla, cuando se le agrega un coma al final.
b = 1,
print b
print type(b)

# Si no se agrega una coma se reconocera como entero
c = (1)
print c
print type(c)

# Se combianan las tuplas de la siguiente forma
newTupla = (1,2,3) + (4,5,6)
print newTupla


# DESEMPAQUETADO DE TUPLAS

numtupla = (10,20)
print numtupla
x, y = numtupla
print x, y

# Intercambiando valores en tupla
a = 100
b = 200
print (a, b)
a, b = b, a
print (a, b)
