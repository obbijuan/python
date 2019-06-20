# Generar errores personalizados puede facilitar el desarrollo de proyectos
class UppercaseError(Exception):
    pass

def check():
    words = ['APPLE', 'orange', 'banana']
    for word in words:
        if word.isupper():
            raise UppercaseError(word)


try:
    check()
except UppercaseError as e:
    print('This is my fault. Go next!') 
