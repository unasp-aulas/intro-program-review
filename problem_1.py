#função, ou seja, fazer uma função - return para retornar o resultado
def main(cargo, salario):

    if cargo == 'junior':
        return salario*.15 + salario
    elif cargo == 'pleno':
        return salario*0.26 + salario
    elif cargo == 'senior':
        return salario*0.34 + salario
    else:
        return -1