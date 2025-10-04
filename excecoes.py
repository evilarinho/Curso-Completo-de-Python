import os
os.system('clear')

# Execeção é um objeto que representa um erro ue ocorreu ao executar o programa.
# Blocos try ... except

"""
• Exception - Classe base para todas as exceções
• ArithmeticError - Classe base para todos os erros que ocorrem em cálculos numéricos
• OverflowError - Um cálculo excedeu o limite máximo de um tipo numérico
• ZeroDivisionError - Lançada quando uma divisão ou módulo por zero é executada em
tipos numéricos
• ImportError - Lançada quando uma declaração import falha
• NameError - Um identificador (nome) não foi encontrado no namespace local ou global
• I0Error - Ocorre quando uma operação de E/S, como ler ou escrever em um arquivo,
falha.
• IndentationError - A indentação não foi aplicada corretamente.
• RecursionError - O interpretador detectou que a profundidade máxima de recursão foi
excedida.
• TypeError - Lançada quando uma função ou operação é inválida para o tipo de dados
especificado.
"""
# try:
#     n1 = int(input('Digite um número: '))
# except ValueError:
#     print('Digite apenas números inteiros')
# else:
#     try:
#         n2 = int(input('Digite outro número: '))
#     except ValueError:
#         print('Digite apenas números inteiros')
#     else:
#         try:
#             r = round(n1 / n2, 2)
#         except ZeroDivisionError:
#             print('Não é possível dividir por zero')
#         else:
#             print(f'Resultado: {r}')

def div(k, j):
    return round(k / j, 2)

if __name__ == '__main__':
    while True:
        try:
            n1 = int(input('Digite um número: '))
            n2 = int(input('Digite outro número: '))
            break
        except ValueError:
            print('Ocorreu um erro ao ler o valor. Tente novamente')
    
    try:
        r = div(n1, n2)
    except ZeroDivisionError:
        print('Não é possível dividir por zero')
    except:
        print|('Ocorreu um desconhecido...')
    else:
        print(f'Resultado: {r}')
    finally:
        print('\nFim do cálculo')








