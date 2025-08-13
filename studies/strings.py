course = "Python Programming"

# Maiúsculas e minúsculas
print(course.upper())
print(course.lower())

# Substituição e contagem
print(course.replace("Python", "Java"))  # "Java Programming"
print(course.count("o"))                  # conta quantos 'o'

# Verificação
print(course.startswith("P"))  # True
print(course.endswith("g"))    # True
print("Python" in course)      # True

# Caracteres
print(len(course)) # Exibe o número de caracteres na string
print(course[0]) # Exibe o caractere 'P'
print(course[-1]) # Exibe o caractere antes do 'P' que no caso é o ultimo caractere da string 'G'
print(course[0:3]) # Exibe os caracteres de 0 a 2

text = "Hello, World!"

print(text[0:5])     # "Hello"
print(text[7:])      # "World!"
print(text[:5])      # "Hello"
print(text[-6:-1])   # "World"
print(text[::-1])    # inverte a string
