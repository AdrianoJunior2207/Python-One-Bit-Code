# Resolucao 1

km = int(input("Qual distancia percorrida?:\n"))

if km <= 200:
    value = float(km * 0.5)
    print(f"O valor da sua passagem sera {value}")
elif km > 200:
    value = float(km * 0.35)
    print(f"O valor da sua passagem sera {value}")


# Resolucao 2

salary = float(input("Qual seu salario?: R$\n"))

if salary > 1250.00:
    increase = 0.1 * salary
    newSalary = 1.1 * salary
    print(f"Voce teve um aumento de R${increase:.2f}, e agora seu salario sera R${newSalary:.2f}")
elif salary <= 1250.00:
    increase = 0.15 * salary
    newSalary = 1.15 * salary
    print(f"Voce teve um aumento de R${increase:.2f}, e agora seu salario sera R${newSalary:.2f}")
else:
    print("Erro! Favor tentar novamente!")
    
    


    
    