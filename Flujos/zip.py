# Con la funcion zip, somos capaces de indicar al bucle
# a que se ejecute a través de las listas y que establezca
# las variables en el mismo orden.
days = ['Mon', 'Tue', 'Wed']
fruits = ['apple', 'banana', 'orange']
drinks = ['cooffe', 'tea', 'beer']

for day, fruit, drink in zip(days, fruits, drinks):
    print (day, fruit, drink)
