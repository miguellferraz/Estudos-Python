# Criando uma Lista
thislist = ["apple", "banana", "cherry"] # Uma lista é formada por colchetes

print("\n", thislist) 

# Os itens da lista são ordenados, alteráveis ​​e permitem valores duplicados.
# Os itens da lista são indexados, o primeiro item tem índice [0], o segundo item tem índice [1], etc.

# Quando dizemos que as listas são ordenadas, significa que os itens têm uma ordem definida e essa ordem não mudará.
# Se você adicionar novos itens a uma lista, eles serão colocados no final da lista.

# A lista é mutável, o que significa que podemos alterar, adicionar e remover itens de uma lista depois que ela foi criada.
# Como as listas são indexadas, elas podem ter itens com o mesmo valor:

thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print("\n", thislist)

print("\n", len(thislist)) # Usamos len() para mostrar o comprimento da lista

# Os itens da lista podem ser de qualquer tipo de dado:
list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]

# Uma lista pode conter diferentes tipos de dados:
list1 = ["abc", 34, True, 40, "male"]

# Da perspectiva do Python, listas são definidas como objetos com o tipo de dados 'list':
mylist = ["apple", "banana", "cherry"]
print("\n", type(mylist))

# Também é possível usar o construtor list() ao criar uma nova lista.

thislist = list(("apple", "banana", "cherry")) # Observe os colchetes duplos
print("\n", thislist)