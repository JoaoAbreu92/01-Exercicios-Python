# Exercício Python 19: Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
# Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.
from random import choice
n1 = input('Qual o primeiro aluno: ')
n2 = input('Qual o segundo aluno: ')
n3 = input('Qual o terceiro aluno: ')
n4 = input('Qual o quarto aluno: ')

lista = [n1, n2, n3, n4]
escolhido = choice(lista)

print('O aluno escolhido para apresentar o trabalho foi {}'.format(escolhido))