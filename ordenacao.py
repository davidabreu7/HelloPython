num1 = int(input('Digite o primeiro valor: '))
num2 = int(input('Digite o segundo valor: '))
num3 = int(input('Digite o terceiro valor: '))

if num1 < num2:
    if num2 < num3:
        print('crescente')
    else:
        print('não esta em ordem crescente')
else:
    print('não esta em ordem crescente')
