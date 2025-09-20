import random
import os

novo_jogo = 's'

while novo_jogo == 's':
    print(f'Bem-vindo ao jogo de adivinhação!')
    print(f'Vocẽ terá três chances para adivinhar um número inteiro entre 1 e 15.')

    # Gerar o número aleatóro secreto
    num = random.randint(1,15)

    # Jogar
    for i in range(3):
        print(f'\nQual a sua escolha?')
        chute = int(input())

        if chute == num:
            print(f'\nParabéns, você acertou')
            break
        elif chute > num:
            print(f'Número alto')
        else:
            print(f'Número baixo')
    # Caso não tenha acertado, revelar o número secreto
    if chute != num:
        print(f'\nO número secreto era o {num}')

    novo_jogo = input(f'Deseja jogar outra vez? S para sim, outra tecla para não ') 
    novo_jogo = novo_jogo.lower() 

    # Limpar tela
    os.system('clear')

