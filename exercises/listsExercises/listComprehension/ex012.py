# Monte uma lista de tuplas (x, y) para x de 0 a 4 e y de 0 a 4, mas apenas quando x != y.

list = [(x, y) for x in range(5) for y in range(5) if x != y]

print(list)