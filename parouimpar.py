vNumeros = []

for i in range(15):
    numero = int(input("digite um numero: "))
    vNumeros.append(numero)
for c in range(15):
    if vNumeros[c] % 2 == 0:
        print(vNumeros[c],"par ")
    else:
        print(vNumeros[c], "impar")
        



