import os

os.system('clear')

# Usando um método recursivo otimizado com cache
# fonte: https://www.datacamp.com/pt/tutorial/fibonacci-sequence-python

# Pra resolver a ineficiência da recursão simples, eu costumo usar cache.
# O Python usa o recurso de cache de memória ( lru_cache ) para guardar
# valores que já foram calculados antes, assim a função não precisa
# refazer o trabalho.

from functools import lru_cache

@lru_cache(maxsize = None)
def fib_cache(n):
    if n == 0:
        return 0  
    elif n == 1:
        return 1
    else:
        return fib_cache(n-1) + fib_cache(n-2)

print(f"The Fibonacci Number is {fib_cache(10)}")

# The Fibonacci Number is 55