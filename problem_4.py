#Escreva um programa para aprovar o empréstimo bancário para compra de uma casa. 
#O programa deve perguntar o valor da casa a comprar, o salário e a quantidade de anos a pagar. 
#O valor da prestação mensal não pode ser superior a 30% do salário. Calcule o valor da prestação 
#como sendo o valor da casa a comprar divido pelo número de meses a pagar.

valor_casa = float(input("Qual o valor da casa? "))  # Não alterar
salario = float(input("Qual é o salário? "))  # Não alterar
anos_pagar = int(input("Pagar em quantos anos? "))  # Não alterar

prestacao = valor_casa/(12*anos_pagar)

if prestacao > salario * 0.3:
    print("Empréstimo não pode ser concedido")
else:
    print(f"Valor da prestação: R$ {prestacao}")