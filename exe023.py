

num = int(input('Insira um numero de 0 a 9999: '))

un = num // 1 % 10
de = num // 10 % 10
ce = num // 100 % 10
mi = num // 1000 % 10
print('Unidade: {}\n'
      'Dezena: {}\n'
      'Centena: {}\n'
      'Milhar: {}'.format(un, de, ce, mi))
