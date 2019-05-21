# Los sets solo permiten un conjunto de elementos unicos
# y los elementos repetidos son eliminados automaticamente.
# Los conjuntos son utiles cuando se requiere buscar puntos
# en comun entre los datos.

a = { 1, 2, 2, 3, 3, 4, 5, 6 }
print type(a)
print a
b = { 2, 3, 3, 6, 7}

print '-----------------------'

print a
print b

# Para 'a', quita los datos de 'b', quedando solo 1, 4 y 7
print a - b
# Para 'b', quita los datos de 'a', quedando solo 7
print b - a

# Busca los elementos que existen en ambos sets
print a & b

# Combina los elementos de 'a' y 'b' sin repetirlos
print a | b

# Muestra los elementos que estan en una de las 2 variables
print a ^ b

print '----- METODOS -----'

s = {1,2,3,4,5}

# Agregar elementos al conjunto
s.add(6)
print s
s.remove(6)
print s
s.clear()
print s
