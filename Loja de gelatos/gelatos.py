# MENU - Será exibido as boas vindas, os valores e tamnhos para que o usuário análise qual opção escolherá.
print('='*54)
print(' ' * 7 + 'Bem-vindo a loja de gelatos da Isabella')
print('='*54)
print("-"*22, end=" ")
print("Cardápio", end=" ")
print("-"*22)
print('-'*54)
print('--------| Tamanho | Cupuaçu (CP) | Açaí (AC) |--------')
print('--------|    P    |    R$ 9.00   |  R$ 11.00 |--------')
print('--------|    M    |    R$ 14.00  |  R$ 16.00 |--------')
print('--------|    G    |    R$ 18.00  |  R$ 20.00 |--------')
print('-'*54)

# Variáveis criadas para acumular e iniciar o loop respectivamente.
total = 0
opcao = 'S'

while opcao == 'S':
    sabor = input('Qual o sabor desejado (CP/AC): ').upper()

    # Condições para verificar e acumular com base no que será escolhido pelo usuário em relação ao tamanho e sabor.
    if sabor == 'CP':
        tamanho = input('Qual o tamanho (P/M/G): ').upper()
        if tamanho == 'P':
            valor = 9
            total += 9
            print('\nVocê escolheu um Cupuaçu no tamanho P: R$ 9.00\n')
        elif tamanho == 'M':
            valor = 14
            total += 14
            print('\nVocê escolheu um Cupuaçu no tamanho M: R$ 14.00\n')
        elif tamanho == 'G':
            valor = 18
            total += 18
            print('\nVocê escolheu um Cupuaçu no tamanho G: R$ 18.00\n')
        else:
            print('Tamanho inválido. Tente novamente!\n')
            continue

    elif sabor == 'AC':
        tamanho = input('Qual o tamanho (P/M/G): ').upper()
        if tamanho == 'P':
            valor = 11
            total += 11
            print('\nVocê escolheu um Açaí no tamanho P: R$ 11.00\n')
        elif tamanho == 'M':
            valor = 16
            total += 16
            print('\nVocê escolheu um Açaí no tamanho M: R$ 16.00\n')
        elif tamanho == 'G':
            valor = 20
            total += 20
            print('\nVocê escolheu um Açaí no tamanho G: R$ 20.00\n')
        else:
            print('Tamanho inválido. Tente novamente!\n')
            continue
        
# condição criada caso o usuário escolha um sabor indisponível
    else:
        print('\nSabor inválido. Tente novamente!\n')
        continue 

 # Variável que define se o loop continua ou para.
    opcao = input('Deseja mais alguma coisa? (S/N)\n').upper()
    while opcao != 'S' and opcao != 'N':
        print('Opção inválida. Escolha S para continuar ou N para sair.')
        opcao = input('Deseja mais alguma coisa? (S/N)\n').upper()

# Finaliza o programa e mostra o total a ser pago.
print(f'\nO valor total a ser pago é de R$ {total}.\n')