# Lista: representa uma sequência de valores
# Sintaxe: nome_lista = [valores]

# notas = [5,7,8,6,9]
# print(notas)
import os
print(os.system('clear'))

n1 = [4,6,7,8,0,3]
n2 = [1,6,3,0,12,11]
valores = n1 + n2
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
planetas = ['Mercurio', 'Vênus', 'Marte', 'Saturno', 'Urano', 'Netuno']
for planeta in planetas:    # planeta é uma variável de interação
    print(planeta)






