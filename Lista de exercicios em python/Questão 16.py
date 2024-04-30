'''12. Modifique o programa anterior de forma a ler um número n. Imprima os n
primeiros números primos.'''

def is_primo(numero):
    if numero <= 1:
        return False
    elif numero <= 3:
        return True
    elif numero % 2 == 0 or numero % 3 == 0:
        return False
    i = 5
    while i * i <= numero:
        if numero % i == 0 or numero % (i + 2) == 0:
            return False
        i += 6
    return True

def encontrar_primos(n):
    primos = []
    numero = 2
    while len(primos) < n:
        if is_primo(numero):
            primos.append(numero)
        numero += 1
    return primos

n = int(input("Digite o valor de n: "))
print("Os", n, "primeiros números primos são:", encontrar_primos(n))
