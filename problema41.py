def primo(n):
    cont = 0
    for i in range(1, n+1):
        if n % i == 0:
            cont+=1
    if cont==2:
        return "é primo"
    else:
        return "não é primo"
            
numero = int(input("digite um numero: "))
a = primo(numero)
print(a)




    