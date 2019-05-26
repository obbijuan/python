# Con un * se convierte en una tupla los argumentos y se usa
# cuando no sabemos cuantos parametros se van a pasar a la funcion
def say_something(*args):
    print (args)


say_something('azul', 'verde', 'blanco')

t = ['Mike', 'Nancy']
say_something(*t)
