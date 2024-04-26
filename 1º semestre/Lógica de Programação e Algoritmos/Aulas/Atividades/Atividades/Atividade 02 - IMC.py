Altura = float(input('Digite sua altura '))
Peso = float(input('Digite seu peso'))

IMC = (Peso / Altura ** 2)
IMC = round(IMC, 2)
print ('O IMC', IMC)
if IMC >= 30:
    print('Cuidado com sua saude')

elif IMC < 30:
    print('Tudo ok com sua saude')
