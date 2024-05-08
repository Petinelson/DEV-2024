import machine
import time


led_vermelho = machine.Pin(14, machine.Pin.OUT)
led_verde = machine.Pin(27, machine.Pin.OUT)

while True:
    time.sleep(1)
    led_verde.value(0)
    led_vermelho.value(1)

    time.sleep(1)
    led_verde.value(1)
    led_vermelho.value(0)