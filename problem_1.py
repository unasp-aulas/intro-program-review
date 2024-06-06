def main(cargo,salario):
    
    if cargo == "junior":
       salario = 1.10 * salario
       return salario
    elif cargo == "pleno":
       salario = 1.20 * salario
       return salario
    elif cargo == "senior":
       salario = 1.30 * salario
       return salario
    else:
        return -1

print(main("senior",1000))