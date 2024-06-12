valor_casa = float(input("Qual o valor da casa? "))
salario = float(input("Qual é o salário? "))
anos_pagar = int(input("Pagar em quantos anos? ")) 

prestacao = valor_casa / (anos_pagar * 12)
if prestacao > salario * 0.30:
  print('Reprovado')
else:
  print('Aprovado')