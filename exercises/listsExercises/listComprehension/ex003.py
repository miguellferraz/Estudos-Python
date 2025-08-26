# Dada a lista:
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
# Crie uma nova lista contendo apenas as frutas que possuem a letra "a".

newlist = [x for x in fruits if "a" in x]

print(newlist)