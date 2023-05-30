def capital(cidade1, cidade2):
    if cidade1 == "curitiba" and cidade2 == "florianopolis":
        return "Portanto, a distância entre as cidade de Curitiba e florianopolis é de 305 km."
    elif cidade1 == "curitiba" and cidade2 == "porto alegre":
        return"Portanto, a distância entre as cidade de Curitiba e Porto Alegre é de 742 km."
    elif cidade1 == "florianopolis" and cidade2 == "porto alegre":
        return "Portanto, a distância entre as cidade de florianopolis e Porto Alegre é de 462 km."
    elif cidade1 == "florianopolis" and cidade2 == "curitiba":
        return "Portanto, a distância entre as cidade de florianopolis e curitiba é de 305 km."
    elif cidade1 == "porto alegre" and cidade2 == "curitiba":
        return "Portanto, a distância entre as cidade de Porto Alegre e curitiba é de 742 km."
    elif cidade1 == "porto alegre" and cidade2 == "florianopolis":
        return "Portanto, a distância entre as cidade de Porto alegre e florianoplois é de 462 km."
    elif cidade1 == cidade2:
        return "0"
    else:
        print("cidade invalida!")
        
cidade1 = input("Digite a cidade de Origem: ")
cidade2 = input("Digite a cidade de Destino: ")

print(capital (cidade1, cidade2))








        


