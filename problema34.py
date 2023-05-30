num = []

for i in range (10):
    num.append(int(input("Insira um numero: ")))

for j in range(10):
    
    if num[j] == 10:
        print("O numero", num[j], "é igual a 10")

    if num[j] > (sum(num)/len(num)):
        print("O numero", num[j], "é maior que a média")

    if num[j] == (sum(num)/len(num)):
        print("O numero", num[j], "é igual a média")

print("A media é",(sum(num)/len(num)))




    






    
    






  

