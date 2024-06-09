# Questão 3
# Escreva um programa que solicite repetidamente que digite um número,
#  os números serão somados e o programa será finalizado quando digitar o número 0.
#  Ao final o programa retorna a soma dos números inseridos.


lista = []
while True:
    pergunta = int(input(f"Digite o número:"))
    if pergunta == 0:
            break
            print('Finalizado.')
    else:
      lista.append(pergunta)

resultado = sum(lista)
print(resultado)