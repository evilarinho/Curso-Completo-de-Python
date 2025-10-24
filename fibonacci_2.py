import os

os.system('clear')

# Usando um método recursivo

# O método recursivo é outra maneira de gerar números de Fibonacci.
# Não é tão rápido quanto o método iterativo para sequências maiores,
# mas é uma ótima maneira de entender a lógica por trás da construção
# da sequência.

# Esse método funciona bem para sequências pequenas, mas pode ficar
# lento conforme a sequência cresce, porque recalcula os mesmos
# valores várias vezes.

# fonte: https://www.datacamp.com/pt/tutorial/fibonacci-sequence-python

def fibonacci_recursive(n):
	if n <= 1:
		return n
	else:
		return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)

num_terms = 10
fibonacci_numbers = []
for i in range(num_terms):
	fibonacci_numbers.append(str(fibonacci_recursive(i)))

print(' '.join(fibonacci_numbers))

# para num_terms = 10
# 0 1 1 2 3 5 8 13 21 34