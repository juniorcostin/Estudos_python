#criar uma promoção para um produto no valor de 100 reais

valor = 100
dia = 0
valor_min = 30
while valor > valor_min:
    dia += 1
    print(f' No dia {dia} o produto vai ser vendido por R${valor}')
    valor -= 5