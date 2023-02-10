#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dolares ela pode comprar. 


real = float(input('quanto dinheiro voce tem na carteira? '))
doll = 3.27
conver = real / doll

print('Você tem {:.2f}R$ na sua carteira\n convertendo para dollares ficaria {:.2f}U$'.format(real, conver))