'''10. Escreva um programa que leia um número e verifique se é ou não um
número primo.'''

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
