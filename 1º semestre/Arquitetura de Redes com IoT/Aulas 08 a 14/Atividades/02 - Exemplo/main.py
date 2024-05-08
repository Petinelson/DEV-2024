import machine
import time

led_vermelho = machine.Pin(14, machine.Pin.OUT)
led_verde = machine.Pin(27, machine.Pin.OUT)
botao = machine.Pin(17, machine.Pin.IN, machine.Pin.PULL_UP)

sentinela = 0

def mudanca_led(sentinela):
    if sentinela % 2 == 0:
        led_verde.value(1)
        led_vermelho.value(0)
    else:
        led_verde.value(0)
        led_vermelho.value(1)

led_vermelho.value(1)
while True:
    estado = botao.value()
    if estado == 0:
        mudanca_led(sentinela)
        sentinela += 1
        print(sentinela)

    time.sleep(0.1)