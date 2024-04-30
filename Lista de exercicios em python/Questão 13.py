n = int(input('numero:'))

fatorial = 1


for i in range(1, n + 1):
    fatorial *= i


print("O fatorial de", n, "é", fatorial)
