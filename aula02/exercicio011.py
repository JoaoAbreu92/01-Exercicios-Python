# Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade
#de tinta necessaria para pintá-la, sabendo que cada litro de tinta, pinta uma área de 2m quadrados.
larg = float(input('Qual a largura da parede? '))
alt = float(input('Qual a altura da parede? '))

area = larg * alt
tinta = area /2 
print('Sua parede tem {}m \n Voce vai precisar de {:.2f} latas de tinta para pintar esta parede'.format(area, tinta))