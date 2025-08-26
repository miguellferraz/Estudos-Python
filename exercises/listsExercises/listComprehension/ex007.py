# Crie uma lista com os quadrados de todos os números de 0 a 10, mas só dos pares.

list = [x**2 for x in range(11) if x % 2 == 0]

print(list)