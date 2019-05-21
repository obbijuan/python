# Los diccionarios son mas rapidos que una lista, si se va a buscar
# por una clave, ya que utiliza hashtable y esto hace mas facil y rapido
# encontrar claves.

d = {'x': 10, 'y': 20}
print type(d)
print d

# Para saber el valor de la llave 'y'
print d['y']

# Para reescribir el valor de la clave 'x'
d['x'] = 100
print d

# Agregar una nueva clave y su valor
d['z'] = 200
print d
d[1] = 100000
print d

# Para establecer un diccionario
print dict(a=10, b=20)

# Tambien se pueden establecer lista de tuplas
print dict([('a',200), ('b', 300)])


# METODOS DE UN DICCIONARIO
print '-------- METODOS ---------'
dd = {'x': 10, 'y': 20}
dd2 = {'x':1000, 'j': 50}
print dd
print dd.keys()
print dd.values()

# Actualizar un diccionario con uno nuevo
print dd
print dd2
dd.update(dd2)
print dd

# Para obtener un clave y sin que devuelva error si no existe
print dd.get('j')
print dd.get('jjj')

# Para borrar un elemento del diccionario
dd.pop('x')
print dd
dd.clear()
print dd

# Buscar una clave en el diccionario
dd = {'x': 10, 'y': 20}
print 'y' in dd

# Copiar un diccionario evitando errores
x = {'x':10}
y = x.copy()
y['x'] = 1000
print (x)
print (y)
