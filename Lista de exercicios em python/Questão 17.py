
n = int(input('numero='))


soma_digitos = sum(int(d) for d in str(n))


digito_verificador = soma_digitos % 10


numero_conta_completo = f"{n:06d}-{digito_verificador}"


print("Número de conta completo:", numero_conta_completo)
