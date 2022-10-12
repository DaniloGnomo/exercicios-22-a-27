nome = str(input('Insira seu nome: '))
mai = nome.upper() #coloca maiuscula
minu = nome.lower() #coloca minuscula
nse = nome.split() # separa em bloco
junt = nome.replace(' ', '') #troca espaços vazios por nada
let = len(junt.strip()) #conta total das letras
pno = nse[0] #pega o primeiro bloco
lpno = len(pno.strip()) #conta as letras do primeiro bloco
print('Nome em maiusculo é: {}\n'
      'O Nome em Minusculo é {}\n'
      'O nome {} possui {} letras\n'
      'O primeiro nome é {}\n'
      'E possui {} letras'
      .format(mai, minu, nome, let, pno,  lpno))
