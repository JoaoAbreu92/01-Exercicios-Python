# Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.
'''
from math import trunc
n = float(input('Digite um valor numérico: '))
num = trunc (n)
print('O valor digitado foi {:.3f} e a sua porção inteira é {}'.format(n, num))
print('O valor digitado foi {:.3f} e a sua porção inteira é {}'.format (n, trunc(n)))'''

n = float(input('Digite um número: '))
print('O valor digitado foi {} e a sua porção interia é {}'.format(n, int(n)))
