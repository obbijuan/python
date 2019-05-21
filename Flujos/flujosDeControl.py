# Como escribir un codigo largo.
# En python existe un regla que debemos limitar el largo
# del codigo a un maximo de 80 caracteres.

x = 1+1+1+1+1+1 \
    +1+1+1+1+1
print x

s = ('aaaaaaaaaa'
    'bbbbbbbbb')
print s
print '----------------------'

x = 10

if x < 10:
    print ('Negativo')
elif x==10:
    print ('10000000')
elif x==10:
    print ('10')
else:
    print ('Positivo')

print '----------------------'

# Python obliga a usar un numero exacto de espacio (4),
# para marcar la identacion e ir a la siguiente sentencia

a = 5
b = 10

if a > 0:
    print ('a es positivo')
    if b > 0:
        print ('b es positivo')
