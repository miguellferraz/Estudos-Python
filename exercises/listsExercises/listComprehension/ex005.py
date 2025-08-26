# Crie uma lista contendo apenas as frutas que possuem até 5 letras.

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if len(x) < 5]

print(newlist)