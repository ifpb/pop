# ler 10 valores (mesma linha), exibir o maior

valores = input().split()
print(valores)

# repita 10 vezes
for i in range(10): # 0 1 2 3 4 5 6 7 8 9 (iteração)
    #print(i, valores[i])
    valores[i] = int(valores[i])

print(valores)
print(max(valores))
print(min(valores))
