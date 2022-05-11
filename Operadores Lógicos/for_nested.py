#é um loop dentro de um loop

for numero1 in range(1,6):
    print('produto ' + str(numero1))
    for numero2 in range(5):
        print(numero1, numero2)

palavra = 'FANTASTICO'

for espaco in palavra:
    print(f' {espaco}' , end='')
