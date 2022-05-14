usuario = input('Digite um nome de usuário: ')
senha = input('Digite uma senha: ')

while usuario == senha:
    print('A senha não pode ser igual ao usuário, digite novamente')
    usuario = input('usuário:')
    senha = input('senha:')
else:
    print('Usuário cadastrado com sucesso!')