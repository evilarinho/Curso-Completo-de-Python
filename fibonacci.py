import os

os.system('clear')

"""
A sequência de Fibonacci também pode ser obtida a partir de uma função recursiva.

Ela inicia com os números 0 e 1, e os valores seguintes são calculados pela soma
dos dois anteriores a ele, como segue:
            0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

Desta forma, podemos derivar a fórmula geral para fibonacci:

# Caso Base:
fibonacci (num) = num, se num <= 1, e
# Caso Recursivo
fibonacci (num) = fibonacci (num - 1) + fibonacci (num - 2), para num > 1.

"""
# Fibonacci sem recursividade
# def fibonacci(num):
#     if num <= 1:
#         return num
#     else:
#         lista = [0, 1]
#         i = 2
#         antes1 = 1
#         antes2 = 0
#         while i < num:
#             prox = antes1 + antes2
#             lista.append(prox)
#             antes2 = antes1
#             antes1 = prox
#             i = i + 1
#         return lista

# Versão aluno Edilson | calculou até 40 números 
# def fibonacci(num):
#     if num <= 1:
#         return num
#     else:            
#         return fibonacci(num - 1) + fibonacci(num - 2)
            

# if __name__ == '__main__':
#     x = int(input('Digite a quantidade de números para calcular a sequência de fibonacci: '))

#     if x <= 1:
#         lista = [0]
#     else:
#         lista = [0, 1]
#         i = 2
#         while i < x:
#             lista.append(fibonacci(i))
#             i = i + 1
    
#     print(f'Segue a seguencia de {x} elementos de fibonacci: {lista}')

# Versão do Prof. Fábio dos Reis

def fibonacci(n):
    if n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        seq_fib = fibonacci(n - 1)
        seq_fib.append(seq_fib[-1] + seq_fib[-2])
        return seq_fib

if __name__ == '__main__':
    try:
        num = int(input('Digite a quantidade de fibonacci a gerar: '))
        res = fibonacci(num)
        print(f'Sequência de Fibonacci gerada: {res}')
    except RecursionError:
        print(f'Deve ser fornecido um numero inteiro positivo válido.')

# para num = 10
# 0 1 1 2 3 5 8 13 21 34


