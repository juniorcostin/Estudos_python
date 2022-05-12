def boas_vidas(nome, quantidade):
    print(f'Olá {nome}')
    print(f'Temos {str(quantidade)} laptops em estoque')


boas_vidas('João', 5)

def boas_vidas_default(nome, quantidade=6):
    print(f'Olá {nome}')
    print(f'Temos {str(quantidade)} laptops em estoque')


boas_vidas_default('João')


def soma(*numeros):
    resultado =0
    for num in numeros:
        resultado += num
    return resultado


x = soma(1,3,4,7)
print(x)

def agencia(**carro):
    return carro

print(agencia(modelo='GOL', cor='BRANCA', motor=1.0, placa=1234))
print(agencia(modelo='GOL', cor='AZUL', motor=1.0))
print(agencia(modelo='GOL', cor='PRETO', motor=1.0, placa=4444))