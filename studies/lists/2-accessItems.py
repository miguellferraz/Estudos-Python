# Acessando uma lista:
thislist = ["apple", "banana", "cherry"]
print("\n", thislist[1]) 

# Indexação Negativa:

# Indexação negativa significa começar do fim
# [-1] refere-se ao último item, [-2] refere-se ao penúltimo item etc.
thislist = ["apple", "banana", "cherry"]
print("\n", thislist[-1])

# Faixa de Índices:

# Você pode especificar um intervalo de índices especificando onde começar e onde terminar o intervalo.
# Ao especificar um intervalo, o valor de retorno será uma nova lista com os itens especificados.

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print("\n", thislist[2:5])

# Ao omitir o valor inicial, o intervalo começará no primeiro item:

# Este exemplo retorna os itens do início até "kiwi", mas NÃO incluindo:

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print("\n", thislist[:4])

# Este exemplo retorna os itens de "cherry" até o final:

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print("\n", thislist[2:])

# Verificando se um item existe na Lista:

# Para determinar se um item especificado está presente em uma lista, use a "in" palavra-chave:

thislist = ["apple", "banana", "cherry"]

if "apple" in thislist:
    print("\nYes, 'apple' is in the Fruits List.")
else:
    print("\nNo, 'apple' is not on the Fruits List")