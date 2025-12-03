def soma():
    soma = 0
    for i in range(0,9,1):
        if i%2 == 0:
            soma = soma + i
    print("Soma: ", soma)