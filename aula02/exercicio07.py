# Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a média

nota1 = int(input('Digite a primeira nota: '))
nota2 = int(input('Digite a segunda nota: '))
nota3 = int(input('Digite a terceira nota: '))
nota4 = int(input('Digite a quarta nota: '))

media = (nota1 + nota2 + nota3 + nota4) / 4

if media < 7:
    print('Se fodeu trouxa, sua média foi {}'.format(media))
else:
    print('mas é um cagada msm! passou com {}'.format(media))

