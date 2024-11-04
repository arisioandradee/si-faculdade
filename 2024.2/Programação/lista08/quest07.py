'''
Um armazém contratou você para desenvolver um algoritmo de controle de tempertura. O algoritmo
deve solicitar a temperatura diária do armazém e verificar se está dentro da faixa segura (de 18ºC
até 25ºC). Exiba um aviso sempre que a temperatura estiver dentro da faixa e também quando ela
estiver fora da faixa. O programa deverá continuar registrando até que seja registrada uma
temperatura estável por cinco dias consecutivos dentro da faixa segura.
'''
diasConsecutivos = 0
diaAnterior = None 

while True:
    tempDiaria = float(input('Informe a temperatura diária do armazém: '))

    if tempDiaria >= 18 and tempDiaria <= 25:
        print(f'A temperatura de {tempDiaria} está na faixa segura!')
        
        if diaAnterior is not None and diaAnterior >= 18 and diaAnterior <= 25:
            diasConsecutivos += 1
        else:
            diasConsecutivos = 1
    else:
        print(f'A temperatura de {tempDiaria} está fora da faixa segura!')
        diasConsecutivos = 0 

    if diasConsecutivos >= 5:
        print('A temperatura está na faixa segura por 5 dias consecutivos!')
        break

    diaAnterior = tempDiaria