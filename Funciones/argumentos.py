# Argumentos con palabras clave
def menu(entree, drink, dessert):
    print('entree = ', entree)
    print('drink = ', drink)
    print('dessert = ', dessert)

menu(entree='beef', dessert='ice', drink='beer')

print('-------------------------')

# Argumentos por defecto
def menu2(entree='beef', drink='wine', dessert='ice'):
    print('entree = ', entree)
    print('drink = ', drink)
    print('dessert = ', dessert)

menu2('chicken', drink='beer')
