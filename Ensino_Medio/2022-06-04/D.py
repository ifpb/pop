n = int(input())
k = int(input())

tempo = k

for i in range(1, n + 1):
    tempo += 5*i
    if tempo > 240:
        print(i - 1)
        exit()

print(n)
