a = int(input())
b = int(input())

cont = 0

while a % b != 0:
    a += 1
    cont += 1

print(cont)
