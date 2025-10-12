import os
from math import sqrt

os.system('clear')

class NumeroNegativoErros(Exception):
    def __init__(self):
        pass

if __name__ =='__main__':
    try:
        num = int(input("Digite um número possitivo: "))
        if num < 0:
            #raise ArithmeticError
            raise NumeroNegativoErros       
    #except ArithmeticError:
    except NumeroNegativoErros:
        print('Foi fornecido um número negativo')
    else:
        print(f'a raiz uadrada de {num} é {sqrt(num)}')
    finally:
        print('Fim do cálculo')




