#Faça um programa que leia um número inteiro qualquer e mostre na tela sua tabuada

n = int(input('Digite um numero: '))
tab = 0
print('=' * 10)
print('Aqui está a tabuada de {}'.format(n))
print('=' * 10)
while (tab <= 10):
    print('{} X {} = {}'.format(tab, n, (tab * n)))
    tab = tab + 1

# forma 02
n = int(input('Digite um número para ver a tabuada: '))
print('{} x {} = {}'.format(n, 1, n*1))
print('{} x {} = {}'.format(n, 2, n*2))
print('{} x {} = {}'.format(n, 3, n*3))
print('{} x {} = {}'.format(n, 4, n*4))
print('{} x {} = {}'.format(n, 5, n*5))
print('{} x {} = {}'.format(n, 6, n*6))
print('{} x {} = {}'.format(n, 7, n*7))
print('{} x {} = {}'.format(n, 8, n*8))
print('{} x {} = {}'.format(n, 9, n*9))
