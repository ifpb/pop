qt_par = 0
qt_impar = 0
qt_positivo = 0
qt_negativo = 0

for i in range(5):
    valor = int(input())

    if (valor % 2 == 0):
        qt_par = qt_par + 1
    else:
        qt_impar = qt_impar + 1

    if (valor > 0):
        qt_positivo = qt_positivo + 1

    if (valor < 0):
        qt_negativo = qt_negativo + 1

print(qt_par, 'valor(es) par(es)')
print(qt_impar,'valor(es) impar(es)')
print(qt_positivo, 'valor(es) positivo(s)')
print(qt_negativo, 'valor(es) negativo(s)')

print('{} valor(es) par(es)'.format(qt_par))
print('{} valor(es) impar(es)'.format(qt_impar))
print('{} valor(es) positivo(s)'.format(qt_positivo))
print('{} valor(es) negativo(s)'.format(qt_negativo))
