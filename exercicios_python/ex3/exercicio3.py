import funcoes_ex3 as fe 
lista_numeros = []
print('\033[33m\tNúmeros repitidos serão ignorados.\033[m')
print('____' * 15)
while True:
    try:
        numeros = int(input('Digite algum número [0 para parar]: '))
        if not numeros == 0:
            lista_numeros.append(numeros)
    except ValueError:
        print('\033[31mDigite apenas números inteiros.\033[m')
        continue 
    else:
        if numeros == 0:
            break 
print('____' * 15)
print('\033[32mQuantidade de números digitados\033[m')
print(f'{fe.contar(set(lista_numeros))} números.')
print('\033[32mQuantidade de números pares e ímpares: \033[m')
print(fe.impar_par(set(lista_numeros)))
print('\033[32mMenor e maior número digitado na lista: \033[m')
print(fe.maior_menor(set(lista_numeros)))
print('\033[32mMédia:\033[m')
print(fe.media(set(lista_numeros)))
print('___' * 15)