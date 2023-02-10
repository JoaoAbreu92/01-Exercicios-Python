# Faça um algoritimo que leia o salário de um funcionário e mostre o novo salário, com  15% de aumento.

salario = float(input('Qual é o salário do funcionário? R$: '))
novo = salario + (salario * 15 / 100)
print('Um funcionario que ganhava R${:.2f}, com 15% de aumento passa a ganhar R${:.2f}'.format(salario, novo))
