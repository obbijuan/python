
count = 0
while True:
    if count >= 5:
        # Un break finaliza un bucle
        break

    if count == 2:
        count += 1
        # Un continue se salta a la siguiente linea y continua
        # en el siguiente bucle
        continue

    print count
    count += 1



count = 0
while count < 5:
    print count
    count += 1
# El 'else' es efectivo en un 'while', si este no finaliza a causa de un 'break'
else:
    print ('Listo')
