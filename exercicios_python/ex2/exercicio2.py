import estrutura as e
notas = list()
alunos = list()
aluno = dict()
while True:
    print('___' * 18)
    nome = e.validar_nome('Seu nome: ')
    nota1 = e.validar_nota('Digite a 1º nota do aluno: ')
    nota2 = e.validar_nota('Digite a 2º nota do aluno: ')
    nota3 = e.validar_nota('Digite a 3º nota do aluno: ')
    notas = [nota1,nota2,nota3]
    e.cadastrar_aluno(aluno,nome,notas)
    e.receber(aluno,alunos)
    while True:
        resposta = input('Continuar? [Sim/Não]: ')
        if resposta in 'SimsimNãoNaonãonao':
            break
        print('\033[31mDigite apenas sim ou não\033[m')
    if resposta in 'NãoNaonãonao':
        break 
print('___' * 18)
print('\tRelatório')
print('___' * 18)
print(f'Alunos cadastrados: {len(alunos)} alunos')
print(f'Média da turma em geral: {e.media_turma(alunos)} pontos ')
print(e.maior_menor_nota(alunos))