idade = int (input("Digite a idade do jogador para saber a sua categoria: "))

if idade <= 13:
    print ("Categoria Infantil")
elif idade <= 17:
    print ("Categoria Juvenil")
else:
    print ("Categoria Sênio")