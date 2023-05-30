#criar um algoritmo que receba a temperatura
#média de cada mês do ano, em centigrados, e
#armazene essas temperaturas em um vetor. Além
#disso, imprimir as temperaturas de todos os meses, a
#maior e a menor temperatura do ano e em que
#mês aconteceram




mes = ["janeiro","fevereiro","março","abril","maio","junho","julho","agosto","setembro","outubro","novembro","dezembro"]
temp = []
tempmax = None
tempmini = None
for i in range(3):
    print(mes[i])
    temp.append(int(input("digite a temperaturas:")))
for i in range(3):
    print(mes[i],":",temp[i])
for i in temp:
    if tempmax is None or i > tempmax:
        tempmax = i
for i in temp:
    if tempmini is None or i < tempmini:
        tempmini = i
        
posimax = temp.index(tempmax)
posimini = temp.index(tempmini)
        
print("a maior temperatura é",tempmax,"pertence a o mes",mes[posimax],"a menor temperatura é",tempmini,"no mes",mes[posimini])












