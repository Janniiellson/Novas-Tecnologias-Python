'''6. Escreva um aplicativo que receba a, b e c, coeficientes de uma
equação dosegundo grau, e calcule as raízes x’ e x” através da 
fórmula de Báskara.'''
import math

a =float (input('defina o valor de A: '))
b =float (input('defina o valor de B: '))
c =float (input('defina o valor de C: '))


delta =((b*b)-4*a*c)

print('\nmostre o valor de delta: ', delta)

Raiz=math.sqrt(delta)

print('\nmostrar raiz de delta', Raiz)

x1=(Raiz)/(2*a)

print('\nmostrar Valor de x¹:',x1)

x2=(-Raiz)/(2*a)

print('\nmostrar valor de x²:',x2)
