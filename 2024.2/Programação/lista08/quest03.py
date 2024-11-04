'''
Uma empresa de produção de periféricos produz mil unidades de mouses por mês. Desenvolva
um algoritmo que solicite a meta de produção semanal e registre o número de mouses produzidos.
Se a meta não for alcançada por três semanas consecutivas, exiba um alerta para o aumento da
produtividade. O fluxo deve continuar até que o total atinja mil unidades.
'''
totalProduzido = 0
semanaAtual = 0
semanasBaixaProdutividade = 0

producaoSemanal = int(input('Informe a meta de produção semanal: '))
inicioPrograma = input('Você deseja iniciar o programa? (sim/nao)').lower()

while inicioPrograma != 'nao' and totalProduzido < 1000:
    mousesProduzidos = int(input('Informe a quantidade de mouses produzidos na semana: '))
    totalProduzido += mousesProduzidos
    semanaAtual += 1

    if mousesProduzidos < producaoSemanal:
        semanasBaixaProdutividade += 1
    else:
        semanasBaixaProdutividade = 0  # Reseta o contador se a meta for atingida

    if semanasBaixaProdutividade == 3:
        print('A produtividade deve ser aumentada!')

    if totalProduzido >= 1000:
        print(f'Total de mouses produzidos: {totalProduzido}. Meta de produção alcançada!')
        break

    inicioPrograma = input('Você deseja iniciar o programa novamente? (sim/nao)').lower()