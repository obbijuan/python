# Listas

lista = [1,2,3,4,5,6,7,8,9]
print lista
print lista[3]
print lista[-1]     # Imprime el ultimo dato
print lista[-2]     # Imprime el penultimo dato
print lista[2:5]    # Imprime un segmento de la lista
print len(lista)    # Imprime la longitud
print list('asdfghjw')
print lista[::2]    # Devuelve numeros impares
print lista[::-1]   # Datos de forma inversa
print '------------------------------'
a = ['a','b','c']
b = [1,2,3]
x = [a,b]
print x                 # Imprime las listas
print x[1]              # Imprime la segunda lista
print x[0][2]           # Imprime el tercer elemento de la primera lista
print '------------------------------'
s = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
s[2:5] = []     # Elimina un segmento de la lista
print s
s[:] = []       # Elimina todos los elementos
print s
print '------------------------------'
n = [1,2,3,4,5,6,7,8,9]
n.append(100)       # Agrega el elemento al final de la lista
print n
n.insert(0,200)     # Agrega un elemento al inicio de la lista
print n
n.pop()             # Elimina el ultimo elemento
print n
n.pop(0)            # Elimina el primer elemento de la lista
print n
del n[2]            # Elinina el elemento de la posicion indicada
print n
r = [1,2,3,3,3,4,5]
r.remove(3)
print r             # Eliina el primer numero repetido
print '------------------------------'
a = [1,2,3,4,5]
b = [6,7,8,9,10]
print a+b
a.extend(b)
print a
