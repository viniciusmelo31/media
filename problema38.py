def calculararea(raio):
    return(3.14*raio**2)
def calcularperimetro(raio):
    return(2*3.14*raio)

raio = int(input("digite o raio: "))
area = calculararea(raio)
perimetro = calcularperimetro(raio)

print("area = ", area)
print("perimetro = ", perimetro)






