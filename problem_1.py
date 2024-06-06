def main(cargo,salario):
    
    if cargo == "junior":
       salario = 1.15 * salario
       return salario
    elif cargo == "pleno":
       salario = 1.26 * salario
       return salario
    elif cargo == "senior":
       salario = 1.34 * salario
       return salario
    else:
        return -1

print(main("senior",1000))