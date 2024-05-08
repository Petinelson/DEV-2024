letra = 's'
while letra == 's':

    print("[1] adição \n[2] subtração\n[3] multiplicacao\n[4] divisão\n[5] modulo")
    n1 = input('Digite a operação que vc quer fazer: ')

    numero1 = int(input('Digite um numero: '))
    numero2 = int(input('Digite o outro numero: '))
    if n1 == '1':
        soma = numero1 + numero2
        print(f'A soma desses números é: {soma}')

    elif n1 == '2':
        subtracao = numero1 - numero2
        print(f'A subtração desses números é: {subtracao}')

    elif n1 == '3':
        multiplicacao = numero1 * numero2
        print(f'A multiplicação desses números é: {multiplicacao}')

    elif n1 == '4':
        divisao = numero1 / numero2
        print(f'A divisao desses números é: {divisao}')

    elif n1 == '5':
        modulo = numero1 % numero2
        print(f'O modulo desses numeros é: {modulo}')

    letra = input('deseja fazer outra conta?[s/n]')
