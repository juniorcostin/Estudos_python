valor_hora = int(input('Informe o valor que você recebe por hora: '))
hora_dia = int(input('informe o total de horas por dia: '))
dias_trabalhados = int(input('Informe a quantidade de dias trabalhados: '))
salario_bruto = float((valor_hora * hora_dia) * dias_trabalhados)
print(f'Seu salário mensal bruto é de R${salario_bruto}')

imposto_renda = salario_bruto - (salario_bruto - (salario_bruto * 11 / 100))

print(f'Você pagou 11% de imposto de renda, portanto R${imposto_renda:,.2f}')

inss = salario_bruto - (salario_bruto - (salario_bruto * 8 / 100))
print(f'Você pagou 8% ao INSS, portanto R${inss:,.2f}')

sindicato = salario_bruto - (salario_bruto - (salario_bruto * 5 / 100))
print(f'Você pagou 5% ao sindicato, portanto R${sindicato:,.2f}')

salario_liquido = salario_bruto - imposto_renda - inss - sindicato
print(f'Seu salário liquido é de R${salario_liquido:,.2f}')