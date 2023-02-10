#exemplo

n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))

soma = n1 + n2
m = n1 * n2
d = n1 / n2 
di = n1 // n2
e = n1 ** n2

print(' A soma é {}, \n O produto é {} \n A divisão é {:.3f}'.format(soma, m, d), end='') # end='' é para nao quebrar a proxima linha
print('\n Divisão inteira {} \n A potência {}'.format(di, e))