letra = 's'
while letra == 's' or 'S':
    cotacao = float(input('Digite a cotação do dollar: '))

    print("---------------------------------------------------------")
    print("---------------Escolha uma Opção-------------------------")
    print("---------------------------------------------------------")

    opção = int(input('1 - Converter dollar para real  2 - Converter real para dollar: '))

    if opção == 1:
        valor = float(input('Digite o valor em dollar a ser convetido para real: '))
        resultado = valor * cotacao
        print(f"O valor em reais é:  {resultado}")
    elif opção == 2:
        valor1 = float(input('Digite o valor em reais a ser convetido para dollar: '))
        resultado1 = valor1 / cotacao
        print(f"O valor em dollar é {resultado1}")
    else:
        print('Digite uma opção válida')

    letra = (input('Deseja continuar [S/N]:'))

