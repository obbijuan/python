# Cuando se usa ** delante del argumento que se declara en la funcion,
# estos desempaquetan como diccionario

def menu(**kwargs):
    for k, v in kwargs.items():
        print(k, v)

menu(entree='beef', drink='coffee')

print('--------------')

def menu2(food, *args, **kwargs):
    print(food)
    print(args)
    print(kwargs)

menu2('banana', 'apple', 'orange', entree='beef', drink='coffee')
