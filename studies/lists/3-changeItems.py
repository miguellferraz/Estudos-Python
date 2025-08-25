# Alterando valor de um item:

# Para alterar o valor de um item específico, consulte o número do índice:

thislist = ["apple", "banana", "cherry"]
thislist[1] = "orange" # Alterando 'banana' por 'orange'
print("\n", thislist)

# Alterando um intervalo de valores de itens:

# Para alterar o valor dos itens dentro de um intervalo específico, defina uma lista com os novos valores e consulte o intervalo de números de índice onde deseja inserir os novos valores:

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"] 
print("\n", thislist)

# Se você inserir mais itens do que substituir, os novos itens serão inseridos onde você especificou, e os itens restantes serão movidos de acordo:

thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"] # Lembre-se que ao utilizar [2:5], por exemplo, a pesquisa começará no índice 2 (incluído) e terminará no índice 5 (não incluído).
print("\n", thislist)

# Se você inserir menos itens do que irá substituir, os novos itens serão inseridos onde você especificou, e os itens restantes serão movidos de acordo:

thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"] # Nesse caso, altera o segundo e o terceiro valor substituindo-os por 'watermelon'
print("\n", thislist)

