# Removendo itens de uma Lista:

# O método remove() remove o item especificado.

thislist = ["apple", "banana", "cherry"]
thislist.remove("apple")
print("\n", thislist)

# Se houver mais de um item com o valor especificado, o remove()método remove a primeira ocorrência:

thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
thislist.remove("banana")
print("\n", thislist)

# Remover índice especificado:

# O método pop() remove o índice especificado.

thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print("\n", thislist)

# Se você não especificar o índice, o método pop() removerá o último item.

thislist = ["apple", "banana", "cherry"]
thislist.pop()
print("\n", thislist)

# A palavra chave 'del' também remove o índice especificado:

thislist = ["apple", "banana", "cherry"]
del thislist[0]
print("\n", thislist)

# 'del' também pode excluir a lista toda

thislist = ["apple", "banana", "cherry"]
del thislist

# Limpar lista:

# O método clear() esvazia a lista.
# A lista ainda permanece, mas não tem conteúdo.

thislist = ["apple", "banana", "cherry"]
thislist.clear()
print("\n", thislist)