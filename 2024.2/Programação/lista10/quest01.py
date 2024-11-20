'''
A biblioteca da UniCatólica precisará reformular seu algoritmo de cálculo de multas por dias atrasados nas
entregas dos livros alugados pelos alunos. O algoritmo deverá solicitar a quantidade de dias em que houve
atrasos e calcular a multa, de acordo com as seguintes condições:
I) Até 3 dias de atraso: R$ 2,00por dia;
II) De 4 a 7 dias de atraso: R$ 3,00 por dia;
III) Acima de 7 dias de atraso: R$ 5,00 por dia.
À medida em que a quantidade de dias de atraso for sendo informada, o valor da multa deve ser informado,
livro a livro. Ao final, o algoritmo TAMBÉM deverá informar a quantidade total das multas.
'''
multa,totalMulta = 0, 0

qtdDias = int(input('Informe quantos dias em atraso: '))

for i in range(0, qtdDias):
    numLivro = int(input(f"Informe o número de dias de atraso do livro {i+1}: "))

    if numLivro <= 3:
        multa = numLivro * 2
        totalMulta += multa
        print(f'O valor da multa é: R${multa:.2f}')
    elif numLivro >4 and numLivro <=7:
        multa = numLivro * 3
        totalMulta += multa
        print(f'O valor da multa é: R${multa:.2f}')
    else:
        multa = numLivro * 5
        totalMulta += multa
        print(f'O valor da multa é: R${multa:.2f}')

print(f'O valor total das multas é: R${totalMulta:.2f}')