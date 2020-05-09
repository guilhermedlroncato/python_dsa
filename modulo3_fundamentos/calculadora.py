def main():
    menu = ('*' * 18) + ' Calculadora Python ' + ('*' * 18) + '\n'
    menu = menu + 'Selecione a operação desejada:\n\n'
    menu = menu + '1 - Soma\n'
    menu = menu + '2 - Subtração\n'
    menu = menu + '3 - Multiplicação\n'
    menu = menu + '4 - Divisão\n'
    print(menu)
    opcao = int(input('Digite sua opção(1/2/3/4): '))
    num1 = float(input('Digite o primeiro numero: '))
    num2 = float(input('Digite o segundo numero: '))
    operacao(num1, num2, opcao)

def operacao(num1, num2, operacao):
    if operacao == 1:
        resultado = f'{num1} + {num2} = {num1 + num2}'
    elif operacao == 2:
        resultado = f'{num1} - {num2} = {num1 - num2}'
    elif operacao == 3:
        resultado = f'{num1} * {num2} = {num1 * num2}'
    else:
        resultado = f'{num1} / {num2} = {num1 / num2}'
    
    print(resultado)   
    
main()