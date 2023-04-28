#inicio da função metragem limpeza

def metragem_limpeza():
    print('--------------- MENU 1 DE 3 - Metragem da limpeza ---------------')
    while True:
      try:
        metragemL = int(input('Digite a metragem desejada:'))
        if (metragemL >= 30 ) and (metragemL <= 300):
          return 60 + 0.3 * metragemL
        if (metragemL >= 300 ) and (metragemL < 700):
          return 120 + 0.5 * metragemL
        else:
            print('Digite um valor válido...')
            continue
      except:
        ValueError 
        print('Digite apenas números!')
        continue

   #Fim Metragem da limpeza

#Inicio do tipo de limpeza
def tipo_limpeza():
    print('--------------- MENU 2 DE 3 - Tipo de limpeza ---------------')
    while True:
      tipolimpeza = input('Qual o tipo de Limpeza desejada: \n'+
                          'B – Básica - Indicada para sujeiras semanais ou quinzenais) \n' +
                          'C – Completa - Indicada para sujeiras antigas e/ou não rotineiras) \n' +
                          '>> ')
      tipolimpeza = tipolimpeza.upper()
      tipolimpeza = tipolimpeza.strip()
      if tipolimpeza == 'B':
        return 1.00
      elif tipolimpeza == 'C':
        return 1.30
      else:
        print('!!!! Selecione uma opção válida !!!!')
        continue # retorna para a pergunta
    #Fim tipo de limpeza

#Inicio do adicional de limpeza
def adicional_limpeza():
    print('--------------- MENU 3 DE 3 - Adicional limpeza ---------------')
    acumulador = 0
    while True:
      adicionalL = input('Deseja algum serviço adicional\n'+
                         '0 - Não desejo mais serviços adicionais (encerrar pedido)\n'+
                         '1- Passar 10 peças de roupas - R$ 10.00\n'+
                         '2- Limpeza de 1 Forno/Micro-ondas - R$ 12,00\n'+
                         '3- Limpeza de 1 Geladeira/Freezer - R$ 20,00\n'+
                         '>>')
                        
      if adicionalL == '0':
        return acumulador
      elif adicionalL == '1':
        acumulador = acumulador + 10
        continue # volta para o while True
      elif adicionalL == '2':
        acumulador = acumulador + 12
        continue # volta para o while True
      elif adicionalL == '3':
        acumulador = acumulador + 20
      else:
        print('digite um valor valido!')
        continue # volta para o while True
                        
     # Fim Adicional limpeza

#inicio do main
print('-------------Bem vindo ao programa de serviços de limpeza do Victor Ramos!------------------------')
metragemL = metragem_limpeza()
tipolimpeza = tipo_limpeza()
adicionalL = adicional_limpeza()
total = (metragemL * tipolimpeza) + adicionalL
print ('O total ficou: R$ {:.2F} (Metragem: R$ {:.2F} * Tipo {} + Adicional: R$ {:.2F})' . format (total,metragemL,tipolimpeza,adicionalL))
