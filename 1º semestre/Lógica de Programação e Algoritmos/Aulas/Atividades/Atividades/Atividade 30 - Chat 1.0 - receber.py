from click import clear
import time

while True:
    clear()
    with open("chat_1.0.txt", "r") as arquivo:
        mensagens = arquivo.readlines()

    for mensagem in reversed(mensagens):
        print(mensagem)
    time.sleep(3)
