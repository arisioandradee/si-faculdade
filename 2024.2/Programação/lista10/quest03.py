'''
Uma empresa deseja calcular o número de defeitos encontrados em sua linha de produção, nos três turnos
em que funciona: manhã (turno 1), tarde (turno 2) e noite (turno 3). Desenvolva um algoritmo que solicite o
número de unidades produzidas e o número de defeitos encontrados em cada um dos turnos. A fórmula
utilizada para o cálculo do índice de defeitos é: índice = (defeitos / produção) * 100. Sabendo disso, o
programa deverá classificar as produções em:
I) Índice menor ou igual a 2%: produção excelente;
II) Acima de 2% até 5%: produção aceitável;
III) Acima de 5%: produção ruim.
Para cada turno e quantide
'''
for i in range(1, 4):
    qtdProduzidas = int(input(f'Informe a quantidade de unidades produzidas no turno {i}: '))
    qtdDefeitos = int(input(f'Informe a quantidade de defeitos encontrados no turno {i}: '))

    if qtdProduzidas > 0:
        indice = (qtdDefeitos / qtdProduzidas) * 100
        if indice <= 2:
            classificacao = 'Produção excelente!'
        elif indice >2 and indice <=5:
            classificacao = 'Produção aceitável!'
        else:
            classificacao = 'Produção ruim!'
    else:
        print('Produção inváldia!')
        continue

    print(f"Turno {i}: Índice de Defeitos = {indice:.2f}% - ({classificacao})")