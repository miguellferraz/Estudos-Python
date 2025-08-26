# Crie uma lista com os quadrados dos números de 0 a 20, mas somente dos números que não são múltiplos de 2 nem de 3.

list = [x**2 for x in range(21) if x % 2 != 0 and x % 3 != 0]

print(list)