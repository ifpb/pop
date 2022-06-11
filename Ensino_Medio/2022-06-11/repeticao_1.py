lista = [] # lista está vazia, não tem índice

while True: # sempre
    senha = int(input())

    lista.append(senha)

    if (senha == 2002):
        print('Acesso Permitido')
        break
    else:
        print('Senha Invalida')

print(lista)
