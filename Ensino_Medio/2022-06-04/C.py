import string

s = input().lower()

alfabeto = string.ascii_lowercase

for letra in alfabeto:
    if letra not in s:
        print('NÃO')
        exit()

print('SIM')
