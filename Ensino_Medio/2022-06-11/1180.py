qtde = int(input()) # 10
valores = input().split()

for i in range(qtde): # 0 1 2 3 4 5 6 7 8 9
    valores[i] = int(valores[i])

menor = min(valores)

print('Menor valor:', menor)

for i in range(qtde):
    if (valores[i] == menor):
        print('Posicao:', i)


