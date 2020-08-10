def calculadora():
    print("########## Calculadora de horas ##########")
    x = 0
    while x == 0:
        x = int(input("""Escolha uma opçao
                          1. Horas em Minutos
                          2. Minutos em Horas  """))
        if x == 1:
            horas = int(input("Horas"))
            minutos = int(input("Minutos"))
            conversor = (horas * 60 + minutos)
            print("Total de minutos:", conversor)
            break
        if x == 2:
            minutos = int((input("Quanto Minutos?")))
            horas_inteiro = minutos // 60
            horas_resto = minutos % 60
            print(minutos, " são %s:%s horas" % (horas_inteiro, horas_resto))
            break
        else:
            print("opcao invalida, digite 1 ou 2")
            x = 0


def main():
    calculadora()


main()
