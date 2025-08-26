# Crie uma lista com os nomes das frutas em fruits, mas apenas aquelas que não têm a letra "a", todas em maiúsculas.

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x.upper() for x in fruits if not "a" in x]

print(newlist)