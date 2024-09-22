'''
Solicite a idade do usuário e classifique-o como "Criança" (idade < 12), "Adolescente" (12 <= idade < 18), 
"Adulto" (18 <= idade < 60) ou "Idoso" (idade >= 60)
'''

idade = int(input('Digite sua idade: '))

if idade < 12:
    print('Criança!')
elif idade >= 12 and idade <18:
    print('Adolescente!')
elif idade >= 18 and idade <60:
    print('Adulto')
else:
    print('Idoso!')