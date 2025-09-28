import os
os.system('clear')

# Set

planeta_anao = {'Plutão', 'Ceres', 'Eris', 'Haumea', 'Makemake'}
# print(planeta_anao)
# print(len(planeta_anao)) 
# print('Ceres' in planeta_anao)
# print('Lua' in planeta_anao)  
# print('Lua' not in planeta_anao)  

#for astro in planeta_anao:
    #print(astro.upper())
    #print(astro.upper(), end='')
    #print(astro.upper(), end=' ')

# Criar uuma lista
#astros = ['Lua', 'Vênus', 'Sirius', 'Marte', 'Lua']
#print(astros, end=' ')
# astro_set = set(astros)
# print(astro_set)

astro1 = {'Lua', 'Vênus', 'Sirius', 'Marte', 'Io'}
astro2 = {'Lua', 'Vênus', 'Sirius', 'Marte', 'Cometa de Halley'}
# print(astro1 == astro2)
# print(astro1 != astro2)

# print(astro1 | astro2)
# print(astro1.union(astro2))

# print(astro1 & astro2)
# print(astro1.intersection(astro2))

# print(astro1 ^ astro2)
# print(astro1.symmetric_difference(astro2))

astro1.add('Urano')
astro1.add('Sol')
print(astro1)
astro1.remove('Io')
print(astro1)
# astro1.remove('Platão')
# KeyError: 'Platão'
astro1.discard('Platão')
astro1.discard('Lua')
print(astro1)
astro1.pop()    #remover um elemento arbitrário/aleatório
print(astro1)
astro1.clear()
print(astro1)

