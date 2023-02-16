#O mesmo professor do desafio 19 quer sortear a ordem de apresentação de trabalhos dos alunos. 
#Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

from random import shuffle

n1 = input('Qual o primeiro aluno: ')
n2 = input('Qual o segundo aluno: ')
n3 = input('Qual o terceiro aluno: ')
n4 = input('Qual o quarto aluno: ')

lista = [n1, n2, n3, n4]
#shuffle = embaralhar
shuffle(lista)
print("A ordem de apresentação dos trabalhos é: ")
print(lista)
