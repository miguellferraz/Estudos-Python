# Dada a matriz:
matriz = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]
# Crie uma lista única contendo todos os elementos da matriz.

lista_flat = [item for sublista in matriz for item in sublista]

print(lista_flat)