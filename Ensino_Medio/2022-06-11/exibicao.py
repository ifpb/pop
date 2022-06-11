v1, v2, v3 = 10, 20, 30

print(v1, v2, v3)
print('{} {} {}'.format(v1, v2, v3))

# 10-20-30
print(v1, v2, v3, sep='-')
print('{}-{}-{}'.format(v1, v2, v3))

valor = 10 / 3  # 3.333333333...
print(valor)
print('{}'.format(valor))
# print(f'{valor}')
print('{:f}'.format(valor))
print('{:.2f}'.format(valor))
