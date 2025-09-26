import os
os.system('clear')

# Dicionários

elemento = {
    'Z': 3,
    'nome': 'Lítio',
    'grupo': 'Metais Alcalinos',
    'densidade': 0.534
} 

# Só funciona "nome", com 'nome' não reconhece
# print(f'Elemento: {elemento["nome"]}')
# print(f'Densidade: {elemento["densidade"]}')
# print(f'O dicionário possui {len(elemento)} elementos.')

# Atualizar uma entrada
elemento['grupo'] = 'Alcalino'
# print(elemento)

# Adicionar uma entrada
elemento['periodo'] = 1
# print(elemento)

# Exclusão de itens em dicionários
# del elemento['periodo']
# print(elemento)

# elemento.clear()
# print(elemento)

# del elemento
# print(elemento)
# NameError: name 'elemento' is not defined

# print(elemento.items())
# for i in elemento.items():
#     print(i)

# print(elemento.keys())
# for i in elemento.keys():
#     print(i)

# print(elemento.values())
# for i in elemento.values():
#     print(i)

for i, j in elemento.items():
    print(f'{i}: {j}')

     

