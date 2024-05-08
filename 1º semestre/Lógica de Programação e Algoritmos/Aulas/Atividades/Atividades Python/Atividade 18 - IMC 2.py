letra = 's'
while letra == 's':

    Altura = float(input('Digite sua altura '))
    Peso = float(input('Digite seu peso'))

    IMC = (Peso / Altura ** 2)
    IMC = round(IMC, 2)
    print ('O IMC', IMC)
    if IMC <= 18.4:
        print('Abaixo do peso')
    elif IMC <= 24.9:
        print('Peso Adequado')
    elif IMC <= 29.9:
        print('Sobrepeso')
    elif IMC <= 34.9:
        print('Obesidade Grau 1')
    elif IMC <= 39.9:
        print('Obesidade Grau 2')
    elif IMC <= 40:
        print('Obesidade Grau 3')

    letra = input('Deseja repetir a letra [s/n]?')
