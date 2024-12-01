quantidade = int(input('Informe quantos alunos serão informados: '))

nomes = []
notas_ap1 = []
notas_ap2 = []

for i in range(quantidade):
    nome = input(f'Informe o nome do aluno {i + 1}: ')
    nota_ap1 = float(input(f'Informe a nota da AP1 do aluno {i + 1}: '))
    nota_ap2 = float(input(f'Informe a nota da AP2 do aluno {i + 1}: '))

    nomes.append(nome)
    notas_ap1.append(nota_ap1)
    notas_ap2.append(nota_ap2)

aprovados = []

for i in range(quantidade):
    media = (notas_ap1[i] + notas_ap2[i]) / 2
    if media >= 7.0:
        aprovados.append(nomes[i])

print("\nAlunos Aprovados:")
for aluno in aprovados:
    print(aluno)