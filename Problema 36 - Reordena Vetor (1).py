lNum=[]
lNum2=[0,0,0,0,0,0,0,0,0,0]
contador1=9
contador2=0

while contador1 >= 0:
    lNum.append(float(input("Digite um número:")))
    lNum2[contador1]=lNum[contador2]
    contador1-=1
    contador2+=1
print("O vetor sem as trocas fica:", lNum)
print("O vetor com as trocas fica:", lNum2)