'''
A Universidade XYZ precisa desenvolver um sistema de votação para as eleições dos Centros Acadêmicos
dos seus cursos, onde cada curso só pode ter, no máximo, três chapas em disputa. Desenvolva um algoritmo
que, inicialmente, pergunte ao responsável pelo início das votações, se ele deja dar início ao pleito. Em caso
positivo, solicite ao usuário que vote em uma das três opções, a partir do número de cada chapa. Se o
número for inválido, exiba uma mensagem informando que o voto foi anulado. O fluxo deve continuar até
que o responsável pelo pleito, queira encerrar a votação a partir de algum comando para este fim. Antes de
iniciar a votação, o sistema deve perguntar os nomes das três chapas (considere que sempre terão três
chapas em disputa).
'''
votosChapa1, votosChapa2, votosChapa3, votosNulos = 0, 0, 0, 0

nomeChapa1 = input('Informe o nome da primeira chapa: ')
numeroChapa1 = int(input('Informe o número da primeira chapa: '))

nomeChapa2 = input('Informe o nome da segunda chapa: ')
numeroChapa2 = int(input('Informe o número da segunda chapa: '))

nomeChapa3 = input('Informe o nome da terceira chapa: ')
numeroChapa3 = int(input('Informe o número da terceira chapa: '))

validacao = input('Você deseja realizar uma votação? (sim/nao)').lower()
print('OBS: Informe o 0 para encerrar a votação!')
while True:
    voto = int(input('Número da chapa que quer votar: '))

    if voto == numeroChapa1:
        votosChapa1 += 1
    elif voto == numeroChapa2:
        votosChapa2 += 1
    elif voto == numeroChapa3:
        votosChapa3 += 1
    else:
        votosNulos += 1

    if voto == 0:
        break

print('--- APURAÇÃO DOS VOTOS ---')
print(f'Votos {nomeChapa1}-{numeroChapa1}: {votosChapa1}')
print(f'Votos {nomeChapa2}-{numeroChapa2}: {votosChapa2}')
print(f'Votos {nomeChapa3}-{numeroChapa3}: {votosChapa3}')
print(f'Votos nulos: {votosNulos}')