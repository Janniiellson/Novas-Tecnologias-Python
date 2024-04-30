'''14. Escreva um aplicativo que lê um inteiro não negativo, calcula e imprime seu
fatorial.n = int(input('numero:'))'''

n = int(input('numero:'))


fatorial = 1

for i in range(1, n + 1):
    fatorial *= i

print("O fatorial de", n, "é", fatorial)
