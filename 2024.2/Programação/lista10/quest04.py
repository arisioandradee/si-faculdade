''' 
Desenvolva um algoritmo que calcule a eficiência de produção de máquinas industriais. O programa,
inicialmente, deve perguntar, quantas máquinas o usuário deseja calcular a eficiência. Em seguida, deve
perguntar o tempo de operação em horas. Após, deve perguntar a produção total da máquina. O cálculo da
eficiência é feito pela fórmula: eficiência = produção total / tempo de operação. Para cada medição da
eficiência da máquina, o programa deve mostrar a quantidade de unidades produzidas por hora e a
classificação de acordo com o que segue:
I) Acima de 100 unidades/hora: “Máxima Eficiência”;
II) Acima 50 e menor que 100 unidades/hora: “Eficiência Moderada”;
III) Abaixo de 50 unidades/hora: “Eficiência Moderada”.
'''

qtdMaquinas = int(input('Informe a quantidade de máquinas que deseja calcular a eficiência: '))

for i in range(0, qtdMaquinas):
    tempo = float(input('Informe o tempo de operação em horas: '))
    producao = float(input('Informe a produção total da máquina: '))

    eficiencia = producao / tempo

    if eficiencia > 100:
        print(f'Quantidade de unidades produzidas por hora: {eficiencia:2f}')
        print(f'Classificação: Máxima Eficiência!')
    elif eficiencia >= 50:
        print(f'Quantidade de unidades produzidas por hora: {eficiencia:2f}')
        print(f'Classificação: Eficiência Moderada!')
    else:
        print(f'Quantidade de unidades produzidas por hora: {eficiencia:2f}')
        print(f'Classificação: Baixa Efiência!')