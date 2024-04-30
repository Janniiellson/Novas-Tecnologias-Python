'''15. O quadrado de um número natural n é dado pela soma dos n primeiros
números ímpares consecutivos. Por exemplo, 1^2 =1, 2^2 = 1+3 etc. Dado
um número n, calcule seu quadrado usando a soma de ímpares ao invés de
produto'''

def calcular_quadrado_por_soma_de_impares(n):
    soma_impares = 0
    proximo_impar = 1

    for _ in range(n):
        soma_impares += proximo_impar
        proximo_impar += 2  

    return soma_impares
n = 3
quadrado = calcular_quadrado_por_soma_de_impares(n)
print(f"O quadrado de {n} é {quadrado}")
