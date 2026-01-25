import funcoes5 as f
notas = list()
alunos = list()
pessoa = dict()
while True:
    print('___' * 15)
    nome = input('Nome: ')
    n1 = f.validar_notas('Digite a sua 1º nota: ')
    n2 = f.validar_notas('Digite a sua 2º nota: ')
    n3 = f.validar_notas('Digite a sua 3º nota: ')
    notas = [n1,n2,n3]
    f.cadastrar(pessoa,nome,notas)
    alunos.append(pessoa.copy())
    while True:
        rs = input('Continuar? [S/N]: ').strip()
        if rs in 'SsNn':
            break
    if rs in 'Nn':
        break 
print('___' * 15)
print('Aluno com maior nota e aluno com menor nota: ')
print(f.info_notas(alunos))
