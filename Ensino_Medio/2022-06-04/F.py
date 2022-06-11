n = int(input())
array = list(map(int, input().split()))
array = [0] + array

def quer_dancar_com(i):
    return array[i]

for a in range(1, n + 1):
    b = quer_dancar_com(a)
    c = quer_dancar_com(b)

    if a == quer_dancar_com(c):
        print('SIM')
        exit()

print('NÃO')
