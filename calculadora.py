import os

def limpar_tela():
    os.system('cls')

def calculadora():
    while True:
        print('\nCalculadora Simples\n')
        print('1 - Soma')
        print('2 - Subtração')
        print('3 - Multiplicação')
        print('4 - Divisão')
        print('S - Sair')
        operacao = input('\nSelecione uma opção ou "s" para sair: \n')

        if operacao == 's' or operacao == 'S':
            limpar_tela()
            print('\nObrigado por utilizar a Calculadora Simples!')
            break

        if operacao not in ['1','2','3','4']:
            limpar_tela()
            print('\nOpção inválida! Tente novamente!')
            continue

        numero_1 = float(input('\nDigite o primeiro número: '))
        numero_2 = float(input('\nDigite o segundo número: '))

        if operacao == '1':
            resultado = numero_1 + numero_2
            limpar_tela()
            print(f'\nO resultado da operação soma é: {resultado}')
        elif operacao == '2':
            resultado = numero_1 - numero_2
            limpar_tela()
            print(f'\nO resultado da operação subtração é: {resultado}')
        elif operacao == '3':
            resultado = numero_1 * numero_2
            limpar_tela()
            print(f'\nO resultado da operação multiplicação é: {resultado}')
        else:
            if numero_2 == 0:
                print('\nDivisões por zero não são possiveis. Tente novamente')
                continue
            else:
                resultado = numero_1 / numero_2
                limpar_tela()
                print(f'\nO resultado da operação divisão é: {resultado}')

if __name__ == '__main__':
    calculadora()