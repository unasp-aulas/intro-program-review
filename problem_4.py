valor_casa = float(input("Qual o valor da casa? "))  # Não alterar
salario = float(input("Qual é o salário? "))  # Não alterar
anos_pagar = int(input("Pagar em quantos anos? "))  # Não alterar

valor_casa = float(input("Qual o valor da casa? "))  # Não alterar
salario = float(input("Qual é o salário? "))  # Não alterar
anos_pagar = int(input("Pagar em quantos anos? "))  # Não alterar

# Questão 4
# Escreva um programa para aprovar o empréstimo bancário para compra de uma casa.
# O programa deve perguntar o valor da casa a comprar, o salário e a quantidade de anos a pagar.
# O valor da prestação mensal não pode ser superior a 30% do salário.
# Calcule o valor da prestação como sendo o valor da casa a comprar divido pelo número de meses a pagar.

while True:
  valor_casa = float(input("Qual o valor da casa? "))  # Não alterar
  salario = float(input("Qual é o salário? "))  # Não alterar
  anos_pagar = int(input("Pagar em quantos anos? "))  # Não alterar


  prestacao = valor_casa / (anos_pagar * 12)
  if prestacao < salario * 0.30:
    print("Aprovado")
  else:
    print('Reprovado')


