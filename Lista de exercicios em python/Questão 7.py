'''7. Escreva um programa que leia a quantidade em segundos e imprima o
resultado em dias, horas, minutos e segundos.'''

print('conversor de segundos')

seg=float(input('escreva o tempo em segundos: '))

dias= seg/86400
hor= seg/3600
min= seg/60

print('mostrar os modelos de hora:')
print('\nsegundos: ',seg)
print('minutos: ',min)
print('horas: ', hor)
print('dias: ', dias)
