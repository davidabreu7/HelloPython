import math

var_a = float(input('Digite o valor de a: '))
var_b = float(input('Digite o valor de b: '))
var_c = float(input('Digite o valor de c: '))

delta = (var_b ** 2) - (4 * var_a * var_c)

if delta > 0:
    x1 = ((-var_b) + math.sqrt(delta)) / (2 * var_a)
    x2 = ((-var_b) - math.sqrt(delta)) / (2 * var_a)
    raiz1 = str(x1)
    raiz2 = str(x2)
    print('''As raizes de %s são: 
    x1 = %s
    x2 = %s''' % (delta, raiz1, raiz2))
elif delta == 0:
    x1 = -var_b / 2 * var_a
    raiz1 = str(x1)
    print('''As raizes de %s são: 
        x1 = %s''' % (delta, raiz1))
else:
    print('Delta = %s' % (delta))
    print('A equação não tem raiz real')
