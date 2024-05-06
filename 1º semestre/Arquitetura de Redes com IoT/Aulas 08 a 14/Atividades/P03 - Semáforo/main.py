import machine
import time

# LED vermelho
vermelho = machine.Pin(26, machine.Pin.OUT)

# LED amarelo
amarelo = machine.Pin(27, machine.Pin.OUT)

# LED verde
verde = machine.Pin(14, machine.Pin.OUT)


while True:
    vermelho.value(0)
    amarelo.value(0)
    verde.value(1)
    time.sleep(5)

    vermelho.value(0)
    amarelo.value(1)
    verde.value(0)
    time.sleep(1)

    vermelho.value(1)
    amarelo.value(0)
    verde.value(0)
    time.sleep(3)
  