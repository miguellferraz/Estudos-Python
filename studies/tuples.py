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

# print(thistuple) # Isso da erro, pois não existe mais "thistuple"

# Desenpacotando uma Tupla:
# O desempacotamento de uma tupla serve para extrair seus elementos e atribuí-los diretamente a variáveis individuais de forma prática e legível.

marcas = ("volkswagen", "chevrolet", "mercedes-benz")

(vw, chevy, amg) = marcas

print(vw) # "volkswagen"
print(chevy) # "chevrolet"
print(amg) # "mercedes-benz"

# Usando asterisco*:
# Se o número de variáveis for menor que a quantidade de valores, é possível adicionar um * antes do nome de uma variável para que os valores excedentes sejam atribuídos a ela como uma lista:

fruits = ("orange", "banana", "apple", "cherry", "strawberry")

(orange, yellow, *red) = fruits

print(orange) # "orange"
print(yellow) # "banana"
print(red) # ['apple', 'cherry', 'strawberry']

# Se o asterisco for adicionado a uma variável que não seja a última, o Python atribuirá valores a ela até que a quantidade de valores restantes corresponda ao número de variáveis ainda não preenchidas.

fruits = ("apple", "mango", "papaya", "pineapple", "cherry")

(green, *tropic, red) = fruits

print(green) # "apple"
print(tropic) # ['mango', 'papaya', 'pineapple']
print(red) # "cherry"

# Loop com Tupla:
# Você pode percorrer os itens da tupla usando um for.

thistuple = ("apple", "banana", "cherry")
for x in thistuple: # Para cada elemento da tupla, atribui o valor à variável 'x'
  print(x) # Exibe o valor atual de 'x' no console

# Juntando Tuplas:
# Para unir duas ou mais tuplas você pode usar o operador "+":

tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3) # ('a', 'b', 'c', 1, 2, 3)

# Multiplicando Tuplas:
# Se você quiser multiplicar o conteúdo de uma tupla um determinado número de vezes, você pode usar o operador "*".

fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2

print(mytuple) # ('apple', 'banana', 'cherry', 'apple', 'banana', 'cherry')

# Métodos de Tupla:
# O Python possui dois métodos internos que podem ser usados em tuplas:
# count()	Retorna quantas vezes um valor específico aparece na tupla.
# index()	Busca um valor específico na tupla e retorna a posição onde ele foi encontrado.

frutas = ("maçã", "banana", "maçã", "cereja")
print(frutas.count("maçã"))  # Saída: 2
# Aqui, o count("maçã") retorna 2 porque "maçã" aparece duas vezes.

frutas = ("maçã", "banana", "cereja")
print(frutas.index("cereja"))  # Saída: 2
# O index("cereja") retorna 2 porque "cereja" está na posição de índice 2