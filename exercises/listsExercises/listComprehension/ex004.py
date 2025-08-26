# Com a mesma lista fruits, crie uma nova lista onde todas as frutas estejam em letras maiúsculas.

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x.upper() for x in fruits]

print(newlist)