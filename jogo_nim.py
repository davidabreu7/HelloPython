def computador_escolhe_jogada(n, m):
    for i in range(1, m + 1):
        if ((n - i) % (m + 1) == 0):
            # print("######")
            # print("O computador tirou %s peças"%str(i))
            return i
        elif i == m:
            # print("O computador tirou %s peças"%str(m))
            return m


def usuario_escolhe_jogada(n, m):
    jogada = 0
    while True:
        try:
            jogada = int(input("Deseja retirar quantas peças? "))
            if jogada > m:
                print("Opção invalida!")
            else:
                break
        except:
            print("Opção invalida!")
            break

    return jogada


def partida():
    usuario = 0
    computador = 0
    qtd_pecas = 0
    max_pecas = 0
    # token = 0
    print("#####")
    while True:
        try:
            qtd_pecas = int(input("Quantas peças? "))
            max_pecas = int(input("Limite de peças por jogada?  "))
            print("#####")
            if qtd_pecas < 0 or max_pecas < 0:
                print("Opção invalida!")
            # elif max_pecas>qtd_pecas:
            #    print("Quantidade de peças deve ser maior que o limite de peças!")
            else:
                break
        except:
            print("Opção invalida!")

    if qtd_pecas % (max_pecas + 1) == 0:
        print("Voce começa!")
        usuario = usuario_escolhe_jogada(qtd_pecas, max_pecas)
        qtd_pecas = qtd_pecas - usuario
        token = 0
        print("######")
        print("Você tirou %s peças" % str(usuario))
        print("Restam %s peças no tabuleiro" % str(qtd_pecas))
    else:
        print("Computador começa!")
        computador = computador_escolhe_jogada(qtd_pecas, max_pecas)
        qtd_pecas = qtd_pecas - computador
        token = 1
        print("######")
        print("Computador tirou %s peças" % str(computador))
        print("Restam %s peças no tabuleiro" % str(qtd_pecas))

    while qtd_pecas > 0:
        if qtd_pecas % (max_pecas + 1) == 0 and token > 0:
            usuario = usuario_escolhe_jogada(qtd_pecas, max_pecas)
            qtd_pecas = qtd_pecas - usuario
            token = 0
            print("######")
            print("Você tirou %s peças" % str(usuario))
            print("Restam %s peças no tabuleiro" % str(qtd_pecas))
        elif token < 1:
            computador = computador_escolhe_jogada(qtd_pecas, max_pecas)
            qtd_pecas = qtd_pecas - computador
            token = 1
            print("######")
            print("Computador tirou %s peças" % str(computador))
            print("Restam %s peças no tabuleiro" % str(qtd_pecas))
    if token == 0:
        print("PARABENS!!! VOCE VENCEU")
        return 0

    else:
        print("Fim do jogo! O computador ganhou!")
        return 1


def main():
    print("Bem vindo ao jogo do NIM! Escolha:")
    print("1 - para cada jogar uma partida isolada")
    print("2- para jogar um campeonato")
    iniciar = 0
    while True:
        try:
            iniciar = int(input("->"))
            if iniciar > 2 or iniciar < 0:
                print("Opção invalida!")
            else:
                break
        except:
            print("Opção invalida!")
    placar = 0
    placar_usuario = 0
    placar_computador = 0
    if iniciar == 1:
        partida()
    else:
        for i in range(1, 4):
            print("############## PARTIDA %s #############" % (str(i)))
            placar = partida()
            if placar == 0:
                placar_usuario = placar_usuario + 1
            else:
                placar_computador = placar_computador + 1
        print("Placar: Você %s X %s Computador" % (str(placar_usuario), str(placar_computador)))


main()
