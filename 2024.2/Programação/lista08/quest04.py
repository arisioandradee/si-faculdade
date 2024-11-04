'''
Você foi contratado para desenvolver um algoritmo de controle de ingestão de calorias com meta
diária. Seu algoritmo deve solicitar a meta de ingestão calórica diária e registrar as calorias
consumidas em cada refeição, informando as calorias acumuladas, a meta e quantas calorias
faltam para atingi-la. O fluxo deve continuar até que o usuário atinja ou ultrapasse a meta diária
(neste caso, exiba uma mensagem informando que o usuário atingiu a meta e a quantidade de
calorias consumidas).
'''
cont, totalCalorias, caloriasLivres = 1, 0, 0
metaDiaria = float(input('Informe a meta diária de calorias: '))

while metaDiaria != 0:
    calorias = float(input(f'Informe o número de caloridas consumidas na sua {cont}° refeição: '))
    cont += 1
    totalCalorias +=  calorias
    caloriasLivres = metaDiaria - totalCalorias
    print(f'Meta de Calorias: {metaDiaria}')
    print(f'Calorias consumidas: {totalCalorias}')
    print(f'Calorias livres : {caloriasLivres}')

    if totalCalorias >= metaDiaria:
        print('Você atingiu sua meta diária!')
        print(f'Calorias consumidas: {totalCalorias:.2f}')