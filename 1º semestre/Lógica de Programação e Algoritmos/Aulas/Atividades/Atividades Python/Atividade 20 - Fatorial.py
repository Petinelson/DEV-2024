numero = int(input('Digite um número para saber o fatorial: '))
resultado = 1
f = 1

while f <= numero:
    resultado *=  f
    f += 1
    print("o fatorial do numero é: ", resultado)