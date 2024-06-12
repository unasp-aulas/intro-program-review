numero = 0
while True:
    numero1 = int(input("Digite um numero, digite 0 para parar de somar: "))
    numero = numero + numero1
    if numero1 == 0:
        print(numero)
        break

