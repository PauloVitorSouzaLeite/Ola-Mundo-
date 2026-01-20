def ler_quantidade(mensagem='Quantidade: '):
    while True:
        try:
            quantidade = int(input(mensagem))
            if not quantidade > 0:
                raise ValueError
        except ValueError:
            print('\033[31mErro. Digite apenas valores inteiros.\033[m')
        else:
            break
    return quantidade

def ler_preco(mensagem):
    while True:
        try:
            numero = float(input(mensagem))
            if not numero > 0:
                raise ValueError
        except ValueError:
            print('\033[31mErro. Digite um preço válido.\033[m')
        else:
            break 
    return numero

def dicionario_recebe(dicionario, nome='Desconhecido', p=0,e=0):
    try:
        dicionario['produto_nome'] = nome 
        dicionario['produto_preco'] = p 
        dicionario['produto_estoque'] = e
        return dicionario
    except Exception as error:
        return f'\033[31mOcorreu um erro: {error}\033[m'

def lista_recebe(lista, dicionario):
    try:
        return lista.append(dicionario.copy())
    except Exception as error: 
        return f'\033[31mOcorreu um erro: {error}\033[m'

def contar(lista=0):
    try:
        return len(lista)
    except Exception as error:
        return f'\033[31mOcorreu um erro.\033[m'

def valor_estoque(lista=0):
    try:
        for produto in lista:
            valor = produto['produto_preco'] * produto['produto_estoque']
            print(f'Nome do produto: \t{produto['produto_nome']} \t| Valor total em estoque: R${round(valor,2)}')
        return '\033[32mCálculo de estoque finalizado!\033[m'
    except Exception as error: 
        return f'\033[31mOcorreu um erro: {error}\033[m'
def caro_barato(lista=0):
    from operator import itemgetter
    try:
        maior = max(lista, key=lambda p: p['produto_preco']) 
        menor = min(lista, key=lambda p: p['produto_preco'])
        return {'produto_maiscaro': maior,
                'produto_maisbarato': menor}
    except Exception as error: 
        return f'\033[31mOcorreu um erro: {error}\033[m'