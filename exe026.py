fra = str.upper(input('Digite uma frase: ')).strip()
nv = fra.count('A')
pv = fra.find('A')+1
uv = fra.rfind('A')+1
print('A letra A aparece: {} de vezes na frase\n'
      'A primeira vez que ela aparece é na posição: {}\n'
      'E a ultima vez que aparece é na posição: {}'.format(nv, pv, uv))
