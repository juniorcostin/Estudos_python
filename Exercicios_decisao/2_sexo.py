sexo = str(input('Aperte F para feminino ou M para masculino: '))
sexo = sexo.upper()
if sexo == str('M'):
    print('Você selecionou masculino')
else:
    if sexo == str('F'):
        print('Você escolheu feminino')
    else:
        print('Opção inválida')