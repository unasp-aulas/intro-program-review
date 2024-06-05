lista = [1, 5, 10, 20]

def main(ultimo_valor):
    
    lista.append(ultimo_valor)
    soma = 0

    for i in lista:  
        soma = i + soma
       
    return soma
    
print(main(1))