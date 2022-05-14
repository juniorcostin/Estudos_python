#Faça um Programa que peça as 4 notas bimestrais e mostre a média.

nota1 = float(input('Informe sua nota do primeiro bimestre: '))
nota2 = float(input('Informe sua nota do segundo bimestre: '))
nota3 = float(input('Informe sua nota do terceiro bimestre: '))
nota4 = float(input('Informe sua nota do quarto bimestre: '))

media = (nota1 + nota2 + nota3 + nota4) / 4

print(f'Sua média deste semestre é: {media}')
