# Usaremos closure cuando queremos apartar un funcion y ejecutarla mas tarde.
# Closure puede ser usado por ejemplo, para establecer un argumento al inicio
# pero podemos introducir un valor en los argumentos mas adelante.

def outer(a, b):

    def inner():
        return a+b

    return inner

f = outer(2, 3)
# Ejecuta la funcion interna
r = f()

print (r)
