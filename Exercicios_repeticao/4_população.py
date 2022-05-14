pop_pais1 = int(input('Informe a população para o país A'))
cresc_pais1 = (float(input('Informe a porcentagem de crescimento desse país: '))/100) * 360
pop_pais2 = int(input('Informe a população para o país B'))
cresc_pais2 = (float(input('Informe a porcentagem de crescimento desse país: '))/100) * 360

print(cresc_pais1)
print(cresc_pais2)
count = 0
while pop_pais1 < pop_pais2:
    pop_pais1 = pop_pais1 + cresc_pais1
    pop_pais2 = pop_pais2 + cresc_pais2
    count += 1

print(f'O país A levará {count} anos para igualar sua população ao país B')