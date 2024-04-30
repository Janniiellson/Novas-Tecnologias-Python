'''3. Escreva um aplicativo que lê um inteiro, determina e imprime se ele é ímpar
ou par.'''

#impar ou par

a = int (input('digite o numero '))

resto =  a % 2 

if resto ==0: 
    print ('par')
else:
    print ('impar')
