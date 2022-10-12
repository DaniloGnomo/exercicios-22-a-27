nom = str.upper(input('Digite seu nome completo: '))
sep = nom.split()
prim = sep[0]
ult = sep.pop()
print('Nome completo: {}\n'
      'Primeiro nome: {}\n'
      'Ultimo nome: {}'.format(nom, prim, ult))
