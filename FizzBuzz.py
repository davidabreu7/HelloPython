numero = int(input('Digite um numero: '))

numero_calc1 = numero % 3
numero_calc2 = numero % 5

if numero_calc1 == 0 and numero_calc2 == 0:
    print('FizzBuzz')
else:
    print(numero)
