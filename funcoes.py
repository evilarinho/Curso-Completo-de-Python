import os
os.system('clear')

# Funções
# Modularização, Reúso de Codigo, Legibilidade

# def mensagem():
#     print('Bóson Treinamentos em Teconologia')
#     print('Curso Completo de Python')

# mensagem()

# Função com argumentos
# def soma(a,b):
#     print(a+b)

# soma(12,7)

# def mult(x, y):
#     return x * y


# a = 5
# b = 8
# c = mult(a, b)
# print(f'O produto de {a} e {b} é {c}')

# def div(k, j):
#     if j != 0:
#         return k / j
#     else:
#         return 'Impossivel dividir por zero'

# if __name__ == '__main__':
#     a = int(input('Digite um número: '))
#     b = int(input('Digite outro número: '))

#     r = div(a, b)
#     print(f'{a} dividido por {b} é igual a {r}')

# def quadrado(val):
#     quadrados = []
#     for x in val:
#         quadrados.append(x ** 2)
#     return quadrados

# if __name__ == '__main__':
#     valores = [2,5,7,9,12]
#     resultados = quadrado(valores)
#     for g in resultados:
#         print(g)

# UDEMY | 28. Funções - Parâmetros opcionais, obrigatórios e valor padrão

# def contar(num=11, caractere='+'):
#     for i in range(1,num):
#         print(caractere)

#if __name__ == '__main__':
    #contar()
    #contar(caractere='&')
    #contar(num=5)
    #contar(num=8, caractere='@')
    #contar(6,'@')
    #contar('#', 8) 
    # TypeError: 'str' object cannot be interpreted as an integer

x = 5
y = 6
z = 3

def soma_mult(a, b, c=0):
    if c == 0:
        return a * b
    else:
        return a + b + c    

if __name__ == '__main__':
    res = soma_mult(x, y)
    print(res)
    res = soma_mult(x, y, z)
    print(res)







    






