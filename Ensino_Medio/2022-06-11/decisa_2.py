# ler três valores (mesma linha) inteiros, exibir o maior

v1, v2, v3 = input().split()
v1, v2, v3 = int(v1), int(v2), int(v3)

if (v1 > v2) and (v1 > v3):
    # v1 é o maior de todos
    if (v2 > v3):
        print(v1, v2, v3)
    else:
        print(v1, v3, v2)
else:
    # v1 não é o maior de todos
    # pode ser o v2 ou pode ser o v3
    if (v2 > v3):
        # v2 é o maior de todos
        if (v1 > v3):
            print(v2, v1, v3)
        else:
            print(v2, v3, v1)
    else:
        # v3 é o maior de todos
        if (v1 > v2):
            print(v3, v1, v2)
        else:
            print(v3,v2,v1)
