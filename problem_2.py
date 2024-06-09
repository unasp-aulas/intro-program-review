# Questão 2
# Escreva uma função main que crie uma sequencia de números e receba um argumento como ultimo número.
# O retorno da função deve ser a soma de todos estes números gerados.

def main(ultimo):
  numeros = []
  for i in range(ultimo + 1):
     numeros.append(i)
     i = i + 1
     soma = sum(numeros)
  return soma