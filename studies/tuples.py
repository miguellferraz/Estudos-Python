# Criando uma tupla:
thisTuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")

print(thisTuple)

print(len(thisTuple)) # Exibe quantos itens existem na Tupla.
print(thisTuple[1]) # Exibe o item de índice 1 - "banana".
print(thisTuple[-1]) # Exibe o último item - "cherry".
print(thisTuple[2:5]) # Exibe o item de índice 2 ao 4 - "cherry", "orange", "kiwi".
print(thisTuple[:4]) # Exibe do item de índice 3 pra trás.
print(thisTuple[2:]) # Exibe do item de índice 2 pra frente.
print(thisTuple[-4:-1]) 

# Checar se um item existe na Tupla:
if "apple" in thisTuple:
  print("Yes, 'apple' is in the fruits tuple")

# Atualizar Tuplas:
# Tuplas são imutáveis, portanto, não é possível alterar diretamente seus valores.
# Porém, existe uma forma simples de contornar isso: transformá-las em uma lista.

x = ("azul", "verde", "vermelho")
y = list(x) # Transforma a Tupla "x" em lista.
y[1] = "amarelo" # Troca "verde" por "amarelo".
x = tuple(y) # Transforma ela de volta em Tupla.

print(x) # ('azul', 'amarelo', 'vermelho')

# Adicionando na Tupla:
# A primeira forma é transformando a em lista e usando append().

thistuple = ("azul", "verde", "vermelho")
y = list(thistuple) 
y.append("amarelo") # Adiciona "amarelo" a lista.
thistuple = tuple(y) # Transforma de volta em Tupla.

# A segunda forma é somando a Tupla com outra Tupla.

thistuple = ("azul", "verde", "vermelho")
y = ("amarelo",) # Cria-se uma nova tupla. (OBS: se houver apenas um item, adicione uma vírgula após ele, pois isso indica que é uma tupla.)
thistuple += y # Soma a Tupla Principal, com a Tupla de item novo.

print(thistuple) # ('azul', 'verde', 'vermelho', 'amarelo')

# Removendo itens de uma Tupla:
# Convertendo-a em uma lista e utilizando o método remove().

thistuple = ("azul", "verde", "vermelho")
y = list(thistuple)
y.remove("azul") # Remove "azul" da Lista
thistuple = tuple(y)
 
# Apagando a Tupla completamente:
# Utilizando o método "del"

thistuple = ("apple", "banana", "cherry")
del thistuple # Deleta "thistuple"

print(thistuple) # Isso da erro, pois não existe mais "thistuple"

