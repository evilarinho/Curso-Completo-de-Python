import os

os.system('clear')

# nome = 'Fábio'
# letra = nome[2]
# print(letra)
# print(len(nome))

# nome = 'Curso de Python'
# instrutor = 'Fábio'
# print(nome + ' com ' + instrutor)

frase = 'Vamos aprender Python hoje.'
#palavras = frase.split()
# print(palavras)
# print(palavras[1])
# for palavra in palavras:
#     print(palavra)
# # for palavra in palavras:
#     print(palavra)
# print(frase[0:5])
# print(frase[6:15])
# print(frase[7:19])
#print(frase[-3:])

# email = input('Digite o seu endereço de email: ')
# arroba = email.find('@')
# print(arroba)
# nome = email[0:arroba]
# dominio = email[arroba+1:]
# print(f'O nome é {nome}')
# print(f'O domínio é {dominio}')

# produtos = 'carbonato de sódio e óxido de zinco'
# print('sódio' in produtos)
# print('magnésio' in produtos)
# print('magnésio' not in produtos)

# item = 'hipoclorito'
# pos = item.find('clo')
# print(pos)
# pos = item.find('flu')
# print(pos)

# objeto_celeste = 'galáxia esPiral M31'
# print(objeto_celeste)
# print(objeto_celeste.upper())
# print(objeto_celeste.lower())
# print(objeto_celeste.capitalize())
# print(objeto_celeste.title())

# suplemento = 'cloero de magnésio'
# n_suplemento = suplemento.replace('magnésio', 'zinco')
# print(suplemento)
# print(n_suplemento)

# remover espaços em branco
# frase = '       ômega 3 é bom para saúde!      '
# print(frase)
# print(frase.lstrip())
# print(frase.rstrip())
# print(frase.strip())

# fruta = 'abacate'
# print(fruta)
# print(fruta.rjust(20))
# print(fruta.center(20))
# print(fruta.ljust(20))
# print(fruta.ljust(20, '-'))
# print(fruta.center(20, '-'))

# p = 'Bóson Treinamentos'
# print(p.startswith('Bó'))
# print(p.startswith('b'))
# print(p.startswith('B'))
# print(p.endswith('s'))
# print(p.endswith('o'))

# Docstrings
"""
Docstring é uma espécie de documentação
que podemos inserir dentro de um módulo, função
ou classe no Python, entre outros locais.
    Respeita deslocamento de texto e é multilinhas
"""

texto = """
Exemplo de Docstring armazeanda em uma variável. 
Não use Docstring como um simples comentário, para isso
use comentário. Use Docstring quando for criar uma função
ou classe que necessite de uma explicação longa sobre a 
sua funcionalidade. 
"""

print(texto)

# Mais sobre manipulação de strings em Python:   
# https://docs.python.org/pt-br/3/library/string.html
