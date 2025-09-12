# num = 1

# while (num <= 10):
#     print(num)
#     num += 1
# print('Laço encerrado!')

nome = None

while True:
    print('Digite o seu nome ou a letra X para parar')
    nome = input()
    if nome.upper() == 'X':
        break
    print(f'Bem-vindo, {nome}')
print('Até logo')

