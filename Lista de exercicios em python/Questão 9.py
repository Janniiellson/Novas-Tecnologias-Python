'''9. Escreva um programa que exiba uma lista de opções (menu): adição,
subtração, divisão, multiplicação e sair. Imprima a tabuada da operação
escolhida. Repita até que a opção saída seja escolhida.'''

print('MENU\n')

print('1-entrar no menu')
print('0-encerrar o programa')


esc=int(input('\n\no que deseja?'))


while esc != 0:	

	if esc==1:
		print('1-Adição: ')
		print('2-Subtração: ')
		print('3-Divisão: ')
		print('4-Multiplicação: ')
		print('0-Sair: ')

		while esc!=0:
			
			slct=int(input('\n\no que deseja fazer: '))
		
			num=int(input('\n\nselecione o numero para que seja efetuada a operação: '))

			if slct==1:
				for i in range(11):
					fim=num+i
					print('operação selecionada: \n',num, '+',i)
					print('\nresultado:',fim, '\n')
					
			elif slct==2:
				for i in range(11):
					fim=num-i
					print(num,'-',i)
					print('\nresultado:',fim, '\n')
					
			elif slct==3:
				for i in range(1,11):
					fim=num/i
					print(num,'/',i)
					print('\nresultado:',fim,'\n')
					
			elif slct==4:
				for i in range(11):
					fim=num*i
					print(num,'x',i)
					print('\nresultado:',fim,'\n')
					

if esc == 0:
	print('encerrando programa...')
elif esc==0:
	print('encerrando programa...')
else:
	print('inválido!!!')
	
