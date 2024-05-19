import desenhos as d
import fileHandler as fH
from random import choice 

def jogar():
    listaPalavras = list()
    arquivo = fH.abrirArquivoLeitura('palavras.txt')
    for linha in arquivo:
        palavra = linha.strip()
        listaPalavras.append(palavra)

    palavraSorteada = choice(listaPalavras)

    for x in range(50):
        print()

    digitadas = []
    acertos = []
    erros = 0

    nome = input('\nQuem está jogando? ')

    while True: 
        adivinha = d.palavraSecreta(palavraSorteada, acertos)

        if adivinha == palavraSorteada:
            print('\nVocê ganhou o jogo!\n')
            break

        tentativa = input('\nDigite uma letra: ').lower().strip()
        if tentativa in digitadas:
            print('\nVocê já usou essa letra!\n')
            continue
        else: 
            digitadas += tentativa 
            if tentativa in palavraSorteada:
                acertos += tentativa
            else: 
                erros += 1
                print('\nVocê errou!\n')
                

        score = d.desenhar(erros)

        if erros == 6:
            print("\nEnforcado!!!\n")
            print(f'\nA palavra certa era: {palavraSorteada}\n')
            break

    fH.inserir_score('score.txt', nome, score)
    