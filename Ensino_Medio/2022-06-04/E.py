n = int(input())
array = input().split()

numeros = list(set(array))

print(len(numeros) - numeros.count("0"))
