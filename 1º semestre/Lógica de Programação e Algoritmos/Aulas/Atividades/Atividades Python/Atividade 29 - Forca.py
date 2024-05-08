from click import clear
palavra = "carro"
palavra_secreta = list("_" * len(palavra))

def menu():
    print("Bem-vindo ao jogo da forca")
    print(f"A palavra possui {len(palavra)} letras")
    #print(" _" * len(palavra))
    print(" ".join(palavra_secreta))

menu()

while "_" in palavra_secreta:
    clear()
    menu()
    chute = input("Chute uma letra: ")
    if chute in palavra:
        indice = 0
        for letra in palavra:
            if chute == letra:
               palavra_secreta[indice] = letra
            indice += 1

    print(" ".join(palavra_secreta))

