letra = 's'
while letra == 's':

    n1 = float(input('digite um número: '))
    n2 = float(input('digite a porcentagem que deseja descobrir: '))

    porcentagem = (n1 * n2) / 100

    print(f'a porcentagem é igual a {porcentagem}: ')

    letra = input('Deseja continuar? [s/n]:')