# Adicionando itens a uma lista:

# Para adicionar um item ao final da lista, use o método append():

thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print("\n", thislist)

# Inserir itens:

# Para inserir um novo item de lista, sem substituir nenhum dos valores existentes, podemos usar o método insert().
# O método insert() insere um item no índice especificado:

thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon") # Inserindo 'watermelon' como terceiro item
print("\n", thislist)

# Estender lista:

# Para acrescentar elementos de outra lista à lista atual, use o método extend().
# Os elementos serão adicionados ao final da lista.

thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print("\n", thislist) 

# Adicionar qualquer iterável
# O método extend() não precisa anexar listas, você pode adicionar qualquer objeto iterável (tuplas, conjuntos, dicionários etc.).

thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print("\n", thislist)

