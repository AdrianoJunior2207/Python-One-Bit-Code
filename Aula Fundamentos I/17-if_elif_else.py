n1 = float(input("Primeiro numero:\n"))
n2 = float(input("Segundo numero:\n"))
operation = int(input("Qual operacao voce quer realizar?\n 1 - SOMA\n 2 - SUBTRACAO\n 3 - MULTIPLICACAO\n 4 - DIVISAO\n"))

if operation == 1:
    print(n1 + n2)
elif operation == 2:
    print(n1 - n2)
elif operation == 3:
    print(n1 * n2)
elif operation == 4:
    print(n1 / n2)
else:
    print("Erro por favor tente novamente!")


    

 