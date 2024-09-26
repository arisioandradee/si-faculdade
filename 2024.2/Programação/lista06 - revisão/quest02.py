'''
Em determinada instituição de ensino, para que o aluno obtenha a aprovação em uma disciplina, é 
necessário realizar duas avaliações e obter a média igual ou superior a 7,0. Desenvolva um algoritmo que 
solicite as duas notas do aluno. Em seguida, verifique a média e exiba uma mensagem de acordo com as 
seguintes condições:
a) Média maior ou igual a 7,0: aluno aprovado.
b) Média maior ou igual a 4,0 e menor do que 7,0: aluno de recuperação.
c) Média menor do que 4,0: aluno reprovado.
'''

n1 = float(input('Digite a nota da AP1: '))
n2 = float(input('Digite a nota da AP2: '))

media = (n1 + n2) /2

if media >= 7:
    print(f'Parabéns! Aluno aprovado com a media: {media:.2f}')
elif media >= 4 and media <7:
    print(f'Aluno em recuperação com a média: {media:.2f}')
else:
    print(f'Aluno reprovado com a media: {media:.2f}')