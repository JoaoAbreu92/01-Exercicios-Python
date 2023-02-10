# Crie um algoritimo que leia um número e mostre o seu dobro, triplo e a raiz quadrada
n1 = int(input('digite um número: '))
dob = n1 * 2
trip = n1 * 3
raiz = n1 ** (1/2)

print('O seu número é {} \n Seu dobro é {} \n Seu triplo é {} \n Sua raiz quadra é {:.2f}'.format(n1, dob, trip, raiz))