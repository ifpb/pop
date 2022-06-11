# ler dois valores (mesma linha) inteiros, exibir o maior

v1, v2 = input().split()
v1, v2 = int(v1), int(v2)

if (v1 > v2):
    print(v1)
else:
    print(v2)

print(max(v1, v2))
