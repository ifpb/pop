# ler 6 valores (mesma linha), exibir o maior

valores = input().split()
print(valores)

valores[0] = int(valores[0])
valores[1] = int(valores[1])
valores[2] = int(valores[2])
valores[3] = int(valores[3])
valores[4] = int(valores[4])
valores[5] = int(valores[5])

print(valores)
print(max(valores))
print(min(valores))
