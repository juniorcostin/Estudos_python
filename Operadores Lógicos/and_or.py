renda_acima_5mil = True
nome_limpo = False
#and depende da confirmação dos dois valores
if renda_acima_5mil and nome_limpo:
    print('Financiamento aprovado')
else:
    print('Financiamento negado')

#or depende da confirmação de apenas um dos valores
if renda_acima_5mil or nome_limpo:
    print('Financiamento aprovado')
else:
    print('Financiamento negado')
