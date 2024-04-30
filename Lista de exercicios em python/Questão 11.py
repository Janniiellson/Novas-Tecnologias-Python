'''11. Coloque um número bem grande para ser executado no exemplo anterior,
você perceberá que demora bastante, consegue pensar num solução na
lógica para reduzir o tempo de procura?'''

num=int(input('escolha um numero:'))

if num >= 1:
    for i in range (1,num):
    if num % i !=0:
            print(num, 'é primo')
    else:
            print(num,'não é primo')
    break
elif num == 0:
	print (num,'não é zero')
else:
	print(num, 'é negativo')
