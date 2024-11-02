numero = int(input('Informe um número: '))

if numero % 3 == 0 and numero % 5 == 0:
    print(f'O número é múltiplo de 3 e de 5!')
elif numero % 3 == 0:
    print(f'O número é múltiplo de 3!')
elif numero % 5 == 0:
    print(f'O número é múltiplo de 5!')
else:
    print(f'O número não é múltiplo nem de 3 nem de 5!')