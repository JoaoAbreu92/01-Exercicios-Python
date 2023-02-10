#Escreva um programa que leia um valor em metros e o exiba convertido em centimetros e milimitros

n1 = int(input('Digite um numero: '))
cm = n1 * 100
mm = n1 *1000
print(' {}m convertido para cm fica {}cm \n convertido para milimetros fica {}mm '.format(n1, cm, mm))