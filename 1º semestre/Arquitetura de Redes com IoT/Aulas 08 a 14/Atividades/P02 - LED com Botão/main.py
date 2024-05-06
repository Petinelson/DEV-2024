import machine
import time

led = machine.Pin(25, machine.Pin.OUT)
botao = machine.Pin(26, machine.Pin.IN, machine.Pin.PULL_UP)

while True:
    estado = botao.value()
    if estado == 0:
        print("botão pressionado!")
        led.value(1)
    else:
        led.value(0)
    time.sleep(0.15)    

