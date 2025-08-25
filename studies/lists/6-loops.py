# Percorrer uma lista:

# Podemos percorrer os itens de uma lista usando o loop 'for'

# Imprima todos os itens da lista, um por um:

thislist = ["apple", "banana", "cherry"]

for x in thislist:
    print(x)

print("---------------")

# Percorrer os números de índice:

# Você também pode percorrer os itens da lista consultando seu número de índice.
# Use as funções range() e len() para criar um iterável adequado.

# Imprima todos os itens consultando seu número de índice:

thislist = ["apple", "banana", "cherry"]

for i in range(len(thislist)):
    print(thislist[i])

print("---------------")

# Usando um loop While:

# Você pode percorrer os itens da lista usando um loop 'while'.

# Use a função len() para determinar o comprimento da lista, comece em 0 e percorra os itens da lista consultando seus índices.
# Lembre-se de aumentar o índice em 1 após cada iteração.

# Imprima todos os itens, usando um loop 'while' para percorrer todos os números de índice.

thislist = ["apple", "banana", "cherry"]

i = 0

while i < len(thislist):
    print(thislist[i])
    i = i + 1