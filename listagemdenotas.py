nomeLista = []
nota1Lista = []
nota2Lista = []
mediaLista = []

for i in range(5):
    nome = (input("qual seu nome? "))
    nomeLista.append(nome)
    nota1 = (float(input("digite a primeira nota:")))
    nota1Lista.append(nota1)
    nota2 = (float(input("digite a primeira nota:")))
    nota2Lista.append(nota2)

    media = (nota1 + nota2) /2

for j in range(5):
    print("ola", nomeLista[j], "sua primeira nota foi", nota1Lista[j], "e sua segunda foi", nota2Lista[j], "entao sua media e", media)






        








