import sys
import os
os.system('clear')

def raizes(a, b, c):
    d = (b**2 - 4*a*c)
    x1 = (-b + d**(1/2)) / (2*a)
    x2 = (-b - d**(1/2)) / (2*a)

    print(f'\nValor de x1: {x1:.2f}')
    print(f'\nValor de x2: {x2:.2f}\n')

    # Opcional: retornar os valors em uma lista
    valores = [x1]
    valores.append(x2)

    return valores

if __name__=='__main__':
    while True:
        print('\nCalcular as raizes de uma equação de 2o grau\n')
        print('Equação no formato ax2 + bx + c = 0\n')

        try:
            a = float(input('Entre com o valor de a (diferente de zero): '))
            b = float(input('Entre com o valor de b: '))
            c = float(input('Entre com o valor de c: '))
        except ValueError:
            print('Digite somente números')
        else:
            if a != 0:
                res = raizes(a,b,c)
                print(res)
            else:
                print('\nATENÇÃO: A não pode ser zero')
        
        while True:
            continua = input('\nDigite q para sair ou n para novo cálculo: ')
            if (continua.lower()) == 'q':
                sys.exit()
            elif (continua.lower() == 'n'):
                os.system('clear')
                break
            else:
                print('Entrada inválida')
                

