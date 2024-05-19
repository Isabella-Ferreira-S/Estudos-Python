import random

def valida_int(pergunta, min, max):
    while True:
        try:
            x = int(input(pergunta))
            if min <= x <= max:
                return x
            else:
                print(f'Por favor, digite um número entre {min} e {max}.')
        except ValueError:
            print('Entrada inválida. Digite um número inteiro.')

def nome_jogada(numero):
    if numero == 1:
        return 'Pedra'
    elif numero == 2:
        return 'Papel'
    elif numero == 3:
        return 'Tesoura'

def vencedor(jogador1, jogador2):
    if jogador1 == jogador2:
        return 0  # empate
    elif (jogador1 == 1 and jogador2 == 3) or (jogador1 == 2 and jogador2 == 1) or (jogador1 == 3 and jogador2 == 2):
        return 1  # jogador1 vence
    else:
        return 2  # jogador2 vence

print('JOKENPO')
print('1- Pedra')
print('2- Papel')
print('3- Tesoura')
print('4 - Encerrar jogadas e verificar o vencedor')

jogadas = []
resultados = [0, 0, 0]  # [v1, v2, empate]

while True:
    j1 = valida_int('Escolha sua jogada: ', 1, 4)
    if j1 == 4:
        print('Saindo...')
        break
    j2 = random.randint(1, 3)
    jogadas.append([j1, j2])
    resultado = vencedor(j1, j2)
    
    if resultado == 1:
        resultados[0] += 1
        print(f'Jogador 1 escolheu {nome_jogada(j1)}, Jogador 2 escolheu {nome_jogada(j2)} (vence Jogador 1)')
    elif resultado == 2:
        resultados[1] += 1
        print(f'Jogador 1 escolheu {nome_jogada(j1)}, Jogador 2 escolheu {nome_jogada(j2)} (vence Jogador 2)')
    else:
        resultados[2] += 1
        print(f'Jogador 1 escolheu {nome_jogada(j1)}, Jogador 2 escolheu {nome_jogada(j2)} (empate)')

for jogada in jogadas:
    print(f'Jogador 1: {nome_jogada(jogada[0])}, Jogador 2: {nome_jogada(jogada[1])}')

print('\nResultados finais:')
print(f'Número de vitórias do Jogador 1: {resultados[0]}')
print(f'Número de vitórias do Jogador 2: {resultados[1]}')
print(f'Número de empates: {resultados[2]}')

if resultados[0] > resultados[1]:
    print('Jogador 1 é o vencedor final!')
elif resultados[1] > resultados[0]:
    print('Jogador 2 é o vencedor final!')
else:
    print('O jogo terminou em empate!')
