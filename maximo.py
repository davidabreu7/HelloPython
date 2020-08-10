def maximo(x, y):
    if x >= y:
        return x
    else:
        return y


def maior_primo(x):
    y = x - 1
    while True:
        if x == 3 or x == 5 or x == 7:
            break
        elif (y % 2 == 0) or (y % 3 == 0) or (y % 5 == 0) or (y % 7 == 0):
            y = y - 1
        else:
            break
    return x


def vogal(x):
    vogais_minus = ['a', 'e', 'i', 'o', 'u']
    vogais_mais = ['A', 'E', 'I', 'O', 'U']
    if (x in vogais_minus) or (x in vogais_mais):
        return True
    else:
        return False


print(str(vogal('U')))
