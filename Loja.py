####################################################
print ('Bem-vindo á sorveteria!')
print ('                                       CARDÁPIO / MENU'                                          )
print ('_________________________________________________________________________________________________')
print ('|CÓDIGO |      DESCRIÇÃO       | TAMANHO P (500 ml) | TAMANHO M (1000 ml) | TAMANHO G (2000 ml) |')
print ('|  TR   | SABORES TRADICIONAIS |............R$ 6,00 |............R$ 10,00 |............R$ 18,00 |')
print ('|  ES   | SABORES ESPECIAIS    |............R$ 7,00 |............R$ 12,00 |............R$ 21,00 |')
print ('|  PR   | SABORES PREMIUM      |............R$ 8,00 |............R$ 14,00 |............R$ 24,00 |')
print ('_________________________________________________________________________________________________')
acumulador = 0

while True:
    tamanho = input('Escolha o tamanho(P/M/G):')
    tamanho = tamanho.upper() # Para identificar siglas Minusculas e Maiusculas
    if tamanho != 'P' and tamanho != 'M' and tamanho != 'G':
        print('Opção invalida! Digite uma opção válida.')
        continue # voltar para o while!

    codigo = input ('Escolha o Código:')
    codigo = codigo.upper() # Para identificar siglas Minusculas e Maiusculas
    if codigo != 'TR' and codigo != 'ES' and codigo != 'PR':
        print('Opção invalida! Digite uma opção válida.')
        continue # voltar para o while!

    if tamanho == 'P' and codigo == 'TR':
        print('Você escolheu Tradicional! tamanho Pequeno R$ 6,00')
        acumulador = acumulador + 6 # Somando o acumulador para somar com 6!
        print('----------------------------------------------')
    elif tamanho == 'M' and codigo == 'TR':
        print('Você escolheu Tradicional! tamanho Médio R$ 10,00')
        acumulador = acumulador + 10
        print('----------------------------------------------')
    elif tamanho == 'G' and codigo == 'TR':
        print('Você escolheu Tradicional! tamanho Grande R$ 18,00')
        acumulador = acumulador + 18
        print('----------------------------------------------')

    elif tamanho == 'P' and codigo == 'ES':
        print('Você escolheu Especial! tamanho Pequeno R$ 7,00')
        acumulador = acumulador + 7 # Somando o acumulador!
        print('----------------------------------------------')
    elif tamanho == 'M' and codigo == 'ES':
        print('Você escolheu Especial! tamanho Médio R$ 12,00')
        acumulador = acumulador + 12
        print('----------------------------------------------')
    elif tamanho == 'G' and codigo == 'ES':
        print('Você escolheu Especial! tamanho Grande R$ 21,00')
        acumulador = acumulador + 21
        print('----------------------------------------------')

    elif tamanho == 'P' and codigo == 'PR':
        print('Você escolheu Premium! tamanho Pequeno R$ 8,00')
        acumulador = acumulador + 8 # Somando o acumulador!
        print('----------------------------------------------')
    elif tamanho == 'M' and codigo == 'PR':
        print('Você escolheu Premium! tamanho Médio R$ 14,00')
        acumulador = acumulador + 14
        print('----------------------------------------------')
    elif tamanho == 'G' and codigo == 'PR':
        print('Você escolheu Premium! tamanho Grande R$ 24,00')
        acumulador = acumulador + 24
        print('----------------------------------------------')
    deseja_acrescentar = input('Deseja acrescentar algo a mais digite (S / ou pressione qualque tecla para encerrar.)?:')
    deseja_acrescentar = deseja_acrescentar.upper() # Para identificar siglas Minusculas e Maiusculas
    if deseja_acrescentar == 'S':
        continue
    else:
        print('O valor total da sua compra: R$ {:.2f}'.format(acumulador))
        break

####################################################