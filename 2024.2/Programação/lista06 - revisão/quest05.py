'''
Desenvolva um algoritmo que peça ao usuário para inserir a sua idade e o seu nível de escolaridade 
(fundamental, médio, superior). Verifique se a pessoa tem mais de 18 anos e nível superior, e exiba se ela 
pode se inscrever em um concurso.
'''

idade = int(input('Digite sua idade:'))
escolaridade = input('Digite sua escolaridade: ').lower()

if (idade >= 18) and (escolaridade == 'superior'):
    print('Usuário autorizado a se inscrever no concurso!')
else:
    print('Usuário não autorizado a se inscrever no concurso!')
