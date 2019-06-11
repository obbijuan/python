
def print_info(func):
    def wrapper(*args, **kwargs):
        print ('start')
        result = func(*args, **kwargs)
        print ('end')
        return result
    return wrapper # Retorno de la funcion interna, como objeto sin que se ejecute.


@print_info
def add_number(a,b):
    return a + b

r = add_number(10, 20)
print(r)
