# Lista: representa uma sequência de valores
# Sintaxe: nome_lista = [valores]

# notas = [5,7,8,6,9]
# print(notas)
import os
print(os.system('clear'))

# n1 = [4,6,7,8,0,3]
# n2 = [1,6,3,0,12,11]
# valores = n1 + n2
# print(valores)
# print(type(valores))
# print(valores[0])
# print(valores[-1])
# print(valores[-2])
# print(valores[-12])
# valores[0] = 9
# valores[0] = -9.5
# print(valores[0])
# print(valores[0:2])
# print(valores[:4])
# print(valores[3:3])  #não exibe nada
# print(valores[3:4])
# print(valores[-2:])
# print(len(valores))
# print(sorted(valores))
# print(sorted(valores, reverse=True))
# print(sum(valores))
# print(max(valores))
# print(min(valores))

# métodos para manipular os dados da lista
# valores.append(13)      # insere um novo elemento no final da lista
# print(valores)
# valores.pop()       # remove o último elemento da lista
# print(valores)
# valores.pop(3)
# print(valores)
# valores.insert(3,21)
# print(valores)
# print(12 in valores)
# print(17 in valores)

#planetas = list()   # cria uma lista vazia | equivale planetas = []
# planetas = ['Mercurio', 'Vênus', 'Marte', 'Saturno', 'Urano', 'Netuno']
# for planeta in planetas:    # planeta é uma variável de interação
#     print(planeta)
'''
Exercício

Crie um script que peça para o usuário digitar o nome de 5 bebidas
favoritas dele, armazenando esses valores em uma lista.

Na sequência, exiba na tela os elementos da lista em ordem alfabética,
um por linha, usando um laço de repetição for.
'''

# print('Digite suas 5 bebidas favoritas')
# bebidas = []
# for i in range(5):
#     print(f'Bebida {i+1}')
#     b = input('Digite o nome de uma bebida: ')
#     bebidas.append(b)

# bebidas.sort()
# print('Listar as bebidas em ordem alfabética:')
# for bebida in bebidas:
#     print(bebida)

# programa do Professor Fábio dos Reis
bebidas = []
for i in range(5):
    print(f'Digite uma bebida favorita:')
    bebida = input()
    bebidas.append (bebida)

bebidas.sort()

print(f'\nBebidas escolhidas: ')
for bebida in bebidas:
    print(bebida)
print(f'\nSaúde! ')








