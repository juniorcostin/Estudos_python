peso = input('Informe o total em quilos que foram pescados: ')
multa = 4.0

if peso > 50:
    peso_multa = (peso - 50) * multa
    print(f'o peso total é de {peso}, você deve pagar um total de R${peso_multa} em multas')
else:
    print(f'O peso total é {peso}')

