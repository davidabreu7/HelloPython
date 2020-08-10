numero = int(input('Digite um numero: '))

numero_calc = numero % 2

if numero_calc == 0:
    print('O numero %s é par' % (str(numero)))
else:
    print('O numero %s é impar' % (str(numero)))
