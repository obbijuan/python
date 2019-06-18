l = [1,2,3]
i = 5


try:
    # l[500]
    l[0]
except IndexError as ex:
    print('Don`t worry: {}'.format(ex))
# Engloba la gran mayoria de excepciones pero no buena idea usarlo.
except Exception as ex:
    print('Other: {}'.format(ex))
# Si el codigo en try se ejecuto sin errores, pasara a ejecutar el else.
else:
    print('Done!')
# Todo es procesado sin que nada lo impida
finally:
    print('Clean up')
