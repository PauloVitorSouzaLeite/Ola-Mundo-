def validar_nome(nome):
        if nome == '':
            raise ValueError
        elif len(nome) < 4:
            raise ValueError

def validar_nota(mensagem='Digite a nota: '):
    while True:    
        try:
            a = float(input(mensagem))
            if a < 0 or a > 10:
                raise ValueError
        except ValueError:
            print('\033[31mErro. A nota precisa estar entre 0 e 10.\033[m')
        else:
            break 
    return a

def validar_nome(mensagem='Nome do aluno: '):
    while True:
        try:
            nome = input(mensagem).strip().title()
            if len(nome) < 4:
                raise ValueError
            elif nome == '':
                raise ValueError
        except ValueError:
            print('\033[31mErro. Nome do aluno muito pequeno ou vazio.\033[m')
        else:
            break
    return nome 

def calcular_media(lista):
    soma = sum(lista)
    return round(soma / len(lista),2)

def media_turma(lista):
    soma = 0
    for pessoa in lista:
        soma += pessoa['media']
    med = round(soma/len(lista), 2)
    return med

def cadastrar_aluno(dicionario,nome,notas):
    dicionario['nome'] = nome
    dicionario['notas'] = notas 
    dicionario['media'] = calcular_media(notas)
    return dicionario 

def receber(dicionario,lista):
    return lista.append(dicionario.copy())

def maior_menor_nota(alunos):
    from operator import itemgetter
    a = max(alunos,key=lambda aluno: aluno['media'])
    b = min(alunos,key=lambda aluno: aluno['media'])
    return {'maior_nota': a,
            'menor_nota': b,}
