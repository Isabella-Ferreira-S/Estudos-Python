import jogo as j
import fileHandler as fH

def mostrarMenu():
    
    print('='*30)
    print(' ' *7 + 'JOGO DA FORCA')
    print('='*30)
    print('\n1 - JOGAR')
    print('2 - SCORE')
    print('3 - SAIR\n')
    print('='*30)

arquivo = 'score.txt'
if fH.existeArquivo(arquivo):
    print('Aquivo localizado!')
else:
    print('Arquivo não existe!')
    fH.criarArquivo(arquivo)

while True:
    mostrarMenu()
    opcao = int(input('\nEscolha a opção desejada: (1/2/3)\n'))

    if opcao == 1:
            print('Iniciar jogo!')
            j.jogar()
    elif opcao == 2:
        print('SCORE: ')
        dados = fH.listarArquivo('score.txt')
        if not dados:
            print('Score vazio.')
        else: 
            i = 1
            for jogador in dados:   
                print(f'{i} -> {jogador.split(';')[0]}, Pontuação: {jogador.split(';')[1].replace('\n', '')}')
                i += 1

    elif opcao == 3:
            print('Encerrando o jogo...')
            break
    else:
            print('Opção inválida. Tente novamente!')
            