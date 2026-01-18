import processamento as p
print('___' * 15)
print('\tCalculadora Básica')
while True:
    print('___' * 15)
    try:
        num = int(input('Primeiro número: '))
    except ValueError:
        print('\033[31mErro. Digite um número válido.\033[m')
    else:
        while True:
            try:
                num1 = int(input('Segundo número: '))
            except ValueError:
                print('\033[31mErro. Digite um número válido.\033[m')
            else:
                break 
        while True:
            escolha = input('[+ - * / 000] Digite a sua escolha: ')
            if escolha not in ['+','-','*','/','000']:
                continue
            break 
        if escolha == '+':
            print(p.somar(num,num1))
        elif escolha == '-':
            print(p.subtrair(num,num1))
        elif escolha == '*':
            print(p.multiplicar(num,num1))
        elif escolha == '/':
            try:
                print(p.dividir(num,num1))
            except ZeroDivisionError:
                print('\033[31mNão é permitido divisão por zero.\033[m')
        elif escolha == '000':
            break 
print('___' * 15)
print('Programa Finalizado')
