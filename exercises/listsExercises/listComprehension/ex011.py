# Dada a lista:

palavras = ["python", "javascript", "java", "csharp", "go", "ruby"]
# Crie uma nova lista com todas as palavras invertidas (ex: "python" → "nohtyp") e que tenham mais de 3 letras.

newlist = [x[::-1] for x in palavras]

print(newlist)