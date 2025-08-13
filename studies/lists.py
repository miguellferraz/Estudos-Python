numbers = [10, 20, 30, 40, 50]

# Acessando elementos
print(numbers[0])   # 10
print(numbers[-1])  # 50
print(numbers[1:4]) # [20, 30, 40]

# Modificando listas
numbers.append(60) # Adiciona na lista
numbers.insert(2, 25) # Insere em um lugar específico
print(numbers)      # [10, 20, 25, 30, 40, 50, 60]

# Remover elementos
numbers.remove(25)
print(numbers.pop()) # remove o último
