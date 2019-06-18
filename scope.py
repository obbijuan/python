animal = 'cat'

def f():
    animal = 'dog'
    print('after', animal)
    # Imprime como un diccionario, todas las variables locales dentro del scope.
    print(locals())

f()
print('global: ', animal)
print('##############################')
print(globals())
