'''
Um nutricionista deseja acompanhar as calorias consumidas por uma pessoa durante uma semana.
Desenvolva um algoritmo que solicite ao usuário a quantidade de calorias consumidas em cada dia e, ao
final, exiba o total de calorias consumidas ao longo da semana.
'''
soma = 0

for i in range(0,7):
    quantidadeDiaria = float(input(f'Informe a quantidade de calorias consumidas no {i+1}° dia: '))
    soma += quantidadeDiaria

print(f'Seu total de caloridas consumidos na semana foi: {soma:.2f}')