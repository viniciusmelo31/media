vsalario = []
soma = 0

for c in range(12):
    salario = int(input("Digite o salário do mês" +str(c+1)+': '))
    vsalario.append(salario)
    soma = soma + salario
    

print("Salário Anual: ", soma)

mediasalario = (soma)/12
print("Média Salarial Mensal: ", mediasalario)

mediasemestre = (vsalario[0] + vsalario[1] + vsalario[2] + vsalario[3] + vsalario[4] + vsalario[5])/6
print("Média Salarial do Primero Semestre: ", mediasemestre)







    