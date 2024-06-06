#função, ou seja, fazer uma função - return para retornar o resultado
def main(cargo, salario):

    if cargo == 'junior' or 'Júnior' or 'Junior':
        return salario*0.15 + salario
    elif cargo == 'pleno' or 'Pleno':
        return salario*0.26 + salario:
    elif cargo == 'senior' or 'Senio' or 'Sênior':
        return salario*0.34 + salario
    else:
        return -1