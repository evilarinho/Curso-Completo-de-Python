import os 
os.system('clear')

# São imutáveis

# tupla = (2,4,6,7,9)
# print(tupla)

halogenios = ('F','CL', 'Br', 'I', 'At')
# print(halogenios)
# print(len(halogenios))
# print(halogenios[3])
# print(halogenios[-1])
gases_nobres = ('He', 'Ne', 'Ar','Xe', 'Kr', 'Rn')
elementos = halogenios + gases_nobres
#print(elementos)
t1 = (5,2,6,8,4,5,6,4,4,0,12,22,3,4,5)
# print(t1.count(5))
# print(t1.count(3))
# print(halogenios[0:2])
# print(halogenios[:3])
# print(halogenios[-2:])
# print('CL' in halogenios)
# print('Fe' in halogenios)
# print(sum(t1))
# print(min(t1))
# print(max(t1))

# Operações não disponíveis em tuplas: .sort(), •append(), •reverse(), •pop()...

# for elemento in elementos:
#     print(f'Elemento químico: {elemento}')

# Criar uma lista a partir e uma tupla

# grupo17 = list(halogenios)
# grupo17[0] = 'H'
# print(grupo17)

grupo1 = ['Li', 'Na', 'K', 'Rb', 'Cs', 'Fr']
alcalinos = tuple(grupo1)
print(alcalinos)
print(type(alcalinos))

#print(sorted(alcalinos))
alcalinos_ordenados = sorted(alcalinos)
print(alcalinos_ordenados)
#print(alcalinos.sort())     #AttributeError: 'tuple' object has no attribute 'sort'
print(type(alcalinos_ordenados))    #<class 'list'>


