import machine
import time

# Configura o pino GPIO 14 como saída
p14 = machine.Pin(14, machine.Pin.OUT)

# Loop para piscar o LED
while True:
    p14.value(1)   # Liga o LED (HIGH)
    time.sleep(1)   # Espera por 1 segundo
    p14.value(0)   # Desliga o LED (LOW)    
    time.sleep(1)   # Espera por 1 segundo
