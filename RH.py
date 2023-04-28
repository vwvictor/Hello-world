#----- inicio variáveis ------#
lista_funcionario = []
codigo_funcionario = 0
#----- fim variáveis ------#

#----- inicio cadastrar_funcionário ------#
def cadastrar_funcionario(codigo):
  print('Boas vindas ao menu de cadastrar funcionario')
  print('Código do Funcionário: {}'.format(codigo))
  nome = input ('Entre com o Nome do Funcionário: ')
  setor = input ('Entre com o Setor: ')
  salario = int(input ('Entre com o Salário: '))
  dicionario_produto = {'Codigo'      : codigo,
                        'Nome'        : nome,
                        'Setor'       : setor,
                        'Salário'     : salario}
  lista_funcionario.append(dicionario_produto.copy())
#----- fim cadastrar_funcionário ------#

#----- inicio consultar_funcionário ------#
def consultar_funcionario():
  print('Boas vindas ao menu de consultar funcionario')
  while True:
    opcao_consultar = input('\nEscolha a opção desejada:\n'+
                            '1- Consultar todos os Funcionário\n'+
                            '2- Consultar Funcionários por ID\n'+
                            '3- Consultar Funcionários por Setor\n'+
                            '4- Retornar\n'+
                            '>>')
    if opcao_consultar == '1':
      print('Você selecionou a opção consultar TODOS os funcionários')
      for funcionario in lista_funcionario:
        print('-----------------------------------')
        for key, value in funcionario.items():
          print('{}: {}'.format(key,value))
        print('-----------------------------------')
    elif opcao_consultar == '2':
      print('Você selecionou a opção consultar Funcionários por ID')
      valor_desejado = int(input('Entre com o ID desejado: '))
      for funcionario in lista_funcionario:
        if funcionario['Codigo'] == valor_desejado:
          print('-----------------------------------')
          for key, value in funcionario.items():
            print('{}: {}'.format(key,value))
        print('-----------------------------------')
    elif opcao_consultar == '3':
      print('Você selecionou a opção consultar Funcionários por Setor')
      valor_desejado = input('Entre com o Setor desejado: ')
      for funcionario in lista_funcionario:
        if funcionario['Setor'] == valor_desejado:
          print('-----------------------------------')
          for key, value in funcionario.items():
            print('{}: {}'.format(key,value))
        print('-----------------------------------')
    elif opcao_consultar == '4':
      return # volta para o main
    else:
      print('Opção invalida!')
      continue 
#----- fim consultar_funcionário ------#

#----- inicio remover_funcionário ------#
def remover_funcionario():
  print('Boas vindas ao menu de remover funcionario')
  valor_desejado = int(input('Entre com o CODIGO ID que deseja remover: '))
  for funcionario in lista_funcionario:
    if funcionario['Codigo'] == valor_desejado:
      lista_funcionario.remove(funcionario)
      print('Funcionário removido')
#----- fim remover_funcionário ------#

#----- inicio main ------#
print ('Bem vindo ao controle de funcionários do Victor Ramos dos santos')
while True: 
  opcao_principal = input('\nEscolha a opção desejada:\n'+
                          '1- Cadastrar Funcionário\n'+
                          '2- Consultar Funcionário\n'+
                          '3- Remover Funcionário\n'+
                          '4- Sair\n'+
                          '>>')
  if opcao_principal == '1':
    codigo_funcionario = codigo_funcionario + 1
    cadastrar_funcionario(codigo_funcionario)
  elif opcao_principal == '2':
    consultar_funcionario()
  elif opcao_principal == '3':
    remover_funcionario()
  elif opcao_principal == '4':
    break
  else:
    print('Opção invalida!')
    continue 
#----- fim main ------#
