from click import clear
clear()
nome = input("Qual seu nome? ")

while True:
    clear()
    mensagem = input("Digite sua mensagem: \n")
    with open("chat_1.0.txt", "a") as arquivo:
        arquivo.write(f"{nome} | {mensagem}\n")

