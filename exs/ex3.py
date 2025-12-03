def maiusculas_palavras(frase):
    frase = "Ola mundo"
    palavras = frase.split()
    maiusculas = []
    for p in palavras:
        maiusculas.append(p.upper())
    return maiusculas

