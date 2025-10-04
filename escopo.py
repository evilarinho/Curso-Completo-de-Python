import os
os.system('clear')

# Escopo Global e Local

var_global = 'Curso Completo de Python'
def escreve_texto():
    global var_global
    var_global = 'Banco de Dados com SQL'
    var_local = 'Fábio dos Reis'
    print(f'Variável Global: {var_global}')
    print(f'Variável Local: {var_local}')

if __name__ == '__main__':
    print('Executar a função escreve_texto()')
    escreve_texto()

    print('Tentar acessar as variáveis diretamente')
    print(f'Variável Global: {var_global}')
    #print(f'Variável Local: {var_local}')
    #NameError: name 'var_local' is not defined. Did you mean: 'var_global'?

