'''
Desenvolva um algoritmo que solicite a idade do usuário. Caso ele seja maior de idade, verifique se o 
usuário obedece às seguintes condições para que possa obter uma carteira de habilitação:
a) Aprovação no exame psicotécnico;
b) Aprovação no exame de legislação;
c) Aprovação no exame de direção.
Ao final, mostre em tela se o usuário está apto ou não a obter sua habilitação.
'''
idade = int(input('Digite sua idade: '))

if idade >= 18:
    # Solicita as aprovações dos exames
    psicotecnico = input('Você foi aprovado no exame psicotécnico? (sim/não) ').lower()
    legislacao = input('Você foi aprovado no exame de legislação? (sim/não) ').lower()
    direcao = input('Você foi aprovado no exame de direção? (sim/não) ').lower()

    # Verifica se o usuário foi aprovado em todos os exames
    if psicotecnico == 'sim' and legislacao == 'sim' and direcao == 'sim':
        print('Você está apto a obter sua habilitação!')
    else:
        print('Você não está apto a obter sua habilitação.')
else:
    print('Você deve ser maior de idade para obter a habilitação.')