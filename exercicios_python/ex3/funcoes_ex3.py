def media(lista=0):
    try:
        a = 0
        for numero in lista:
            a += numero
        return round(a / len(lista),2)
    except ZeroDivisionError:
        print('\033[31mNão há como fazer cálculos, a lista está vazia.\033[m')

def maior_menor(lista=0):
    try:
        maior = max(lista)
        menor = min(lista)
        dicionario = {'maior_numero': maior, 
                  'menor_numero': menor}
        if lista == None:
            raise ValueError
    except (ValueError , UnboundLocalError):
        print('\033[31mNão há como fazer cálculos, a lista está vazia.\033[m')
    else:
        for chave, valor in dicionario.items():
            print(f'{chave} -> {valor}')
    return ''

def impar_par(lista=0):
    try:
        par = impar = 0
        for numero in lista:
            if numero % 2 == 0:
                par += 1
            else:
                impar += 1
        dicionario = {'numeros_impares': impar,
                  'numeros_pares': par}
    except UnboundLocalError:
        print('\033[31mNão há como fazer cálculos, a lista está vazia.\033[m')
    else:
        for chave, valor in dicionario.items():
            print(f'{chave} -> {valor}')
    return ''

def contar(lista=0):
    return len(lista)