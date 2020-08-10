from itertools import cycle


def alarme():
    print("#### PYTHON ALARME #####")
    alarme_calc = 0
    while True:
        print("Qual o horário atual?")
        horas = int(input("Horas: "))
        alarme = int(input("Alarme em quantas horas? "))

        if (horas >= 0 and horas < 24):
            alarme_calc = alarme + horas
            break
        else:
            print("Hora Invalida")

    if alarme_calc < 24:
        str(alarme_calc)
        print("Alarme setado para as %s:00 horas de hoje." % (alarme_calc))
    else:
        dias = (alarme_calc // 24)
        horas = (alarme_calc % 24)
        str(dias)
        str(horas)
        print("alarme setado para %s dias e %s horas" % (dias, horas))


def dias_semana():
    semana = ('domingo', 'segunda', 'terca', 'quarta', 'quinta', 'sexta', 'sabado')
    dia_chegada = str(input('qual o dia da sua chegada?'))
    while True:
        if dia_chegada in semana:
            estadia = int(input('Quantos dias pretende ficar?'))
            semana_calc = semana.index(dia_chegada)
            semana_ciclo = cycle(semana)
            for i in range(0, estadia):
                print(next(semana_ciclo))
            break
        else:
            print('''Dia da semana inválido.
            Digite: domingo, segunda, terça, quarta, quinta, sexta ou sábado
            
            ''')
            dia_chegada = str(input('qual o dia da sua chegada? '))


def main():
    #  exercicio 1  print(str(alarme()))
    dias_semana()


main()
