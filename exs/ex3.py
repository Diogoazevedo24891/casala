def maiusculas_palavras():
    frase = input("Digite uma frase: ")
    palavras = frase.split()
    maiusculas = []
    for p in palavras:
        maiusculas.append(p.upper())

    print("Palavras em maiúsculas:")
    for p in maiusculas:
        print(p)
