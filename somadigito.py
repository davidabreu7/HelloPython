numero = int(input('Digite o número inteiro: '))
ultimoDigito = 0
tiraDigito = numero
while (tiraDigito != 0):
    ultimoDigito = (tiraDigito % 10) + ultimoDigito
    tiraDigito = tiraDigito // 10

print(ultimoDigito)
