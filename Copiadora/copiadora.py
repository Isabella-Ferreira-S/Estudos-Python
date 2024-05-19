# Início do MENU com mensagem de boas vindas e identificação com nome
print('\nBem-vindo a Copiadora da Isabella\n')
total = 0

def escolha_servico():
    ''' 
        Descrição da função:
         Essa função exibi as opções de serviços e pede que o usário escolha uma delas, também trata as opções inválidas.
        Returns:
            Retorna o serviço escolhido pelo usuário.
    '''
    global total
    while True:
        print('DIG - Serviço de Digitalização')
        print('ICO - Serviço de Impressão Colorida')
        print('IPB - Serviço de Impressão Preto e Branco')
        print('FOT - Serviço de Fotocópia\n')
        servico = input('Qual o serviço desejado:').upper()
        if servico != 'DIG' and servico != 'ICO' and servico != 'IPB' and servico != 'FOT':
            print('\nEscolha inválida, escolha o serviço desejado novamente:\n')
            continue
        elif servico == 'DIG':
           print('\nServiço de Digitalização (DIG) o custo por página é de um real e dez centavos.')

        elif servico == 'ICO':
           print('\nServiço de Impressão Colorida (ICO) o custo por página é de um real.')

        elif servico == 'IPB':
           print('\nServiço de Impressão Preto e Branco (IPB) o custo por página é de quarenta centavos')

        elif servico == 'FOT':
           print('\nServiço de Fotocópia (FOT) o custo por página é de vinte centavos.')

        return servico

def num_pagina(servico):
    ''' 
        Descrição da função
    
    Args:
        parametro1: opção de serviço escolhida pelo usuário na função escolha_servico().
        
    Returns:
        Retorna a quantidade de páginas, o valor do serviço escolhido e o total com o desconto aplicado.
    '''
    while True: 
        try:
            pag = int(input("\nDigite o número de páginas: "))
            if pag > 20000:
                print("\nNão aceitamos tantas páginas de uma vez. Por favor, digite o número de páginas novamente.")
                continue
            else: 
                if (servico == 'DIG'):
                    if (pag < 20):
                        total = pag * 1.10
                        valor = 1.10
                        print (f'\nNão houve desconto! Preço do serviço em relação as páginas informadas: R$ {float(total)}')
                    elif (pag >= 20 and pag < 200):
                        total = (pag * 1.10) - ((pag * 1.10)* 0.15)
                        valor = 1.10
                        print (f'\nVocê ganhou um desconto de 15%! Preço do serviço com desconto em relação as páginas informadas: R$ {float(total)}')
                    elif (pag >= 200 and pag <= 2000):
                        total = (pag * 1.10) - ((pag * 1.10)* 0.20)
                        valor = 1.10
                        print (f'\nVocê ganhou um desconto de 20%! Preço do serviço com desconto em relação as páginas informadas: R$ {float(total)}')
                    elif (pag >= 2000 and pag < 20000):
                        total = (pag * 1.10) - ((pag * 1.10)* 0.25)
                        valor = 1.10
                        print (f'\nVocê ganhou um desconto de 25%! Preço do serviço com desconto em relação as páginas informadas: R$ {float(total)}')
                elif (servico == 'ICO'):
                    if (pag < 20):
                        total = pag 
                        valor = 1
                        print (f'\nNão houve desconto! Preço do serviço em relação as páginas informadas: R$ {float(total)}')
                    elif (pag >= 20 and pag < 200):
                        total = (pag * 1) - ((pag * 1)* 0.15)
                        valor = 1
                        print (f'\nVocê ganhou um desconto de 15%! Preço do serviço com desconto em relação as páginas informadas: R$ {float(total)}')
                    elif (pag >= 200 and pag <= 2000):
                        total = (pag * 1) - ((pag * 1)* 0.20)
                        valor = 1
                        print (f'\nVocê ganhou um desconto de 20%! Preço do serviço com desconto em relação as páginas informadas: R$ {float(total)}')
                    elif (pag >= 2000 and pag < 20000):
                        total = (pag * 1) - ((pag * 1)* 0.25)
                        valor = 1
                        print (f'\nVocê ganhou um desconto de 25%! Preço do serviço com desconto em relação as páginas informadas: R$ {float(total)}')
                elif (servico == 'IPB'):
                    if (pag < 20):
                        total = pag * 0.40 
                        valor = 0.40
                        print (f'\nNão houve desconto! Preço do serviço em relação as páginas informadas: R$ {float(total)}')
                    elif (pag >= 20 and pag < 200):
                        total = (pag * 0.40) - ((pag * 0.40)* 0.15)
                        valor = 0.40
                        print (f'\nVocê ganhou um desconto de 15%! Preço do serviço com desconto em relação as páginas informadas: R$ {float(total)}')
                    elif (pag >= 200 and pag <= 2000):
                        total = (pag * 0.40) - ((pag * 0.40)* 0.20)
                        valor = 0.40
                        print (f'\nVocê ganhou um desconto de 20%! Preço do serviço com desconto em relação as páginas informadas: R$ {float(total)}')
                    elif (pag >= 2000 and pag < 20000):
                        total = (pag * 0.40) - ((pag * 0.40)* 0.25)
                        valor = 0.40
                        print (f'\nVocê ganhou um desconto de 25%! Preço do serviço com desconto em relação as páginas informadas: R$ {float(total)}')
                elif (servico == 'FOT'):
                    if (pag < 20):
                        total = pag * 0.20
                        valor = 0.20
                        print (f'\nNão houve desconto! Preço do serviço em relação as páginas informadas: R$ {float(total)}')
                    elif (pag >= 20 and pag < 200):
                        total = (pag * 0.20) - ((pag * 0.20)* 0.15)
                        valor = 0.20
                        print (f'\nVocê ganhou um desconto de 15%! Preço do serviço com desconto em relação as páginas informadas: R$ {float(total)}')
                    elif (pag >= 200 and pag <= 2000):
                        total = (pag * 0.20) - ((pag * 0.20)* 0.20)
                        valor = 0.20
                        print (f'\nVocê ganhou um desconto de 20%! Preço do serviço com desconto em relação as páginas informadas: R$ {float(total)}')
                    elif (pag >= 2000 and pag < 20000):
                        total = (pag * 0.20) - ((pag * 0.20)* 0.25)
                        valor = 0.20
                        print (f'\nVocê ganhou um desconto de 25%! Preço do serviço com desconto em relação as páginas informadas: R$ {float(total)}')
            return total, valor, pag      
        except: 
            print('\nInsira apenas valores numéricos!')

def servico_extra(parametros):
    ''' 
        Descrição da função
    
    Args:
        parametro1: quantidade de páginas, o valor do serviço escolhido e o total com o desconto aplicado - informações retiradas da função num_pagina().
        
    Returns:
        Retorna uma mensagem informativa com valor total a pagar, o serviço escolhido * a quantidade de páginas e o valor somado como extra.
    '''
    global total
    while True: 
        print('Deseja adicionar algum serviço:')
        print('1 - Encadernação Simples - R$ 15.00')
        print('2 - Encadernação Capa Dura - R$ 40.00')
        print('0 - Não desejo mais nada!')
        extra = int(input(''))
        if (extra == 1):
            total = parametros[0] + 15
            extra = 15
            return f'\nTotal: R${float(total)} (serviço: {parametros[1]} * páginas: {parametros[2]} + extra: {extra} - desconto)\n'
        elif (extra == 2):
            total = parametros[0] + 40
            extra = 40
            return f'\nTotal: R${float(total)} (serviço: {parametros[1]} * páginas: {parametros[2]} + extra: {extra} - desconto)\n'
        elif (extra == 0):
            return 'Encerrando...'
        else:
            print('\nPor favor, selecione uma opção válida.')
            continue
       
# variáveis e print criados para chamar as funções corretamente
servico_selecionado = escolha_servico()
paginas_selecionadas = num_pagina(servico_selecionado)
print(servico_extra(paginas_selecionadas))