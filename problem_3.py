#escrever, quer dizer input - print para retornar resultado
#Escreva um programa que solicite repetidamente que digite um número, os números serão somados 
#e o programa será finalizado quando digitar o número 0. Ao final o programa retorna a soma dos números inseridos.

soma = 0

while True:
      numero = int(input("Digite um número: "))
      if numero == 0:
            break
      soma = soma + numero