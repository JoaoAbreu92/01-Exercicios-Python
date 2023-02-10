
# Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e seu antecessor
n = int(input('Digite um numero: '))
ant = n - 1
sus = n + 1
print('O numero digitado foi {} \n O seu antecessor é {} \n O seu sucessor é {}'.format(n, ant, sus))

#forma 2

n = int(input('Digite um numero: '))
print('O numero digitado foi {} \n O seu antecessor é {} \n O seu sucessor é {}'.format(n, (n+1), (n+2)))
