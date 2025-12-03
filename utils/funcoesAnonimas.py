def funcoesAnonimas():
    soma = lambda a, b: a + b
    print(soma(2,3))

def funcoesAnonimas2():
    quadrados = list(map(lambda x: x**2, range(5)))
    print(quadrados)
