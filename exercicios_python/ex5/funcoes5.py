def cadastrar(dicionario,nome='???',notas=0):
    if notas:
        dicionario['nome'] = nome
        dicionario['notas'] = notas 
        dicionario['média'] = round(sum(notas) / len(notas),2)
        return dicionario
    return 'Nada aqui para calcular.'

def validar_notas(mensagem='Nota: '):
    while True:
        try:
            nota = float(input(mensagem))
            if nota < 0 or nota > 10:
                raise ValueError
        except ValueError:
            print('\033[31mErro\033[m')
        else:
            break
    return nota
def info_notas(lista):
    from operator import itemgetter
    maior_nota = max(lista, key=lambda n: n['média'])
    menor_nota = min(lista, key=lambda n: n['média'])
    return maior_nota, menor_nota