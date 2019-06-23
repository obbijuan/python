# Al encontrar el archivo __init__.py, python reconocerá como paquete y
# podrá importar el archivo utils.py. El archivo __init__.py es escencial
# para crear un paquete

# import modulos.ustils
from modulos import utils

r = utils.say_twice('hellow')
print(r)
