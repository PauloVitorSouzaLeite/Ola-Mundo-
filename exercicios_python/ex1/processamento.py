def somar(num1,num2):
    return num1 + num2 

def subtrair(num1,num2):
    return num1 - num2 

def multiplicar(num1, num2):
    return num1 * num2

def dividir(num1,num2):
    if num1 == 0 or num2 == 0:
        raise ZeroDivisionError
    return round(num1 / num2, 2)