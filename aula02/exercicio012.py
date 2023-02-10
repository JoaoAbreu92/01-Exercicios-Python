#Faça um algoritimo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto

preco = float(input(' Qual o preco do produtoR$? '))
desconto = preco - (preco * 5 / 100)
print('O valor fica {} R$'.format(preco))
print('O valor com o desconto é de {}'.format(desconto))