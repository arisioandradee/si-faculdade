'''
1) Solicite um número ao usuário e verifique se ele é múltiplo de 3, de 5, ou de ambos. Exiba uma mensagem 
correspondente
'''

numero = int(input('Digite um número: '))

if numero % 3 == 0 and numero % 5 == 0:
    print(f'O número {numero} é múltiplo de 3 e de 5.')
elif numero % 3 == 0:
    print(f'O número {numero} é múltiplo de 3.')
elif numero % 5 == 0:
    print(f'O número {numero} é múltiplo de 5.')
else:
    print(f'O número {numero} não é múltiplo de 3 ou 5.')
