nome = input('Digite seu nome: ')
while len(nome) < 3:
    print('O nome deve conter mais de 3 letras, digite novamente: ')
    nome = input('Digite seu nome: ')
else:
    print('nome cadastrado')

idade = int(input('Digite a sua idade: '))
while idade < 0 and idade < 150:
    print('Idade inválida, digite novamente')
    nome = input('Digite seu nome: ')
else:
    print('Idade cadastrada')

salario = float(input('Digite seu salário: '))
while salario < 0:
    print('Salário invalido')
else:
    print('Salario cadastrado')

sexo = input('Informe F para feminino e M para masculino: ')
sexo = sexo.upper()
while sexo != 'F' and sexo != 'M':
    print('Sexo inválido, informe novamente')
    sexo = input('Informe F para feminino e M para masculino: ')
    sexo = sexo.upper()
else:
    print('Sexo cadastrado com sucesso!')

estado_civil = input('informe S para solteiro, C para casado, V para viuvo e D para divorciado: ')
estado_civil = estado_civil.upper()
while estado_civil != 'S' and estado_civil != 'C' and estado_civil != 'V' and estado_civil != 'D':
    Print('Opção inválida, digite novamente')
    estado_civil = input("Informe S para solteiro, C para casado, V para viuvo, D para divorciado: ")
    estado_civil = estado_civil.upper()
else:
    print('Estado civil cadastrado com sucesso')

print('Cadastro finalizado com sucesso')
