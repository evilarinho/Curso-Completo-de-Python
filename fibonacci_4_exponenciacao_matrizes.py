import os

os.system('clear')

# Maneiras mais avançadas de fazer a sequência de Fibonacci em Python

# Exponenciação de matrizes

# A exponenciação matricial é uma das maneiras mais eficientes de calcular
# os números de Fibonacci para valores grandes de n. Em vez de recalcular
# os termos várias vezes, esse método usa a multiplicação de matrizes para
# chegar aos resultados em tempo logarítmico.

# fonte: https://www.datacamp.com/pt/tutorial/fibonacci-sequence-python

import numpy as np

def fibonacci_matrix(n):
	def matrix_power(matrix, power):
		return np.linalg.matrix_power(matrix, power)
	if n == 0:
		return 0
	matrix = np.array([[1, 1], [1, 0]])
	result = matrix_power(matrix, n-1)
	return result[0][0]

fibonacci_numbers = []

for i in range(5000):
	fibonacci_numbers.append(str(fibonacci_matrix(i)))

print(' '.join(fibonacci_numbers))

# para range 10
# 0 1 1 2 3 5 8 13 21 34