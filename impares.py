numero = int(input('Digite o valor de n: '))
contador = 2 * numero
for i in range(0, contador):
    impar = i % 2
    if impar != 0:
        print(i)
