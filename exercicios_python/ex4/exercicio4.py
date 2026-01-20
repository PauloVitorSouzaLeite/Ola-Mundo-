import funcoes as fs
produto = dict()
lista_produtos = list()
while True:
    print('___' * 15)
    nome = input('Digite o nome: ')
    preco = fs.ler_preco('Digite o preço do produto: ')
    estoque = fs.ler_quantidade('Digite o estoque do produto: ')
    fs.dicionario_recebe(produto, nome, preco, estoque)
    fs.lista_recebe(lista_produtos, produto)
    while True:
        resposta = input('Deseja continuar? ').strip()
        if resposta in 'SsNn':
            break
        print('\033[31mApenas S ou N.\033[m')
    if resposta in 'Nn': 
        break
print('___' * 30)
print(f'Quantidade de produtos: {fs.contar(lista_produtos)}')
print(fs.valor_estoque(lista_produtos))
print(fs.caro_barato(lista_produtos))
