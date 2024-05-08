#from machine import Pin, I2C
import machine
import ssd1306
from time import sleep


led_vermelho = machine.Pin(25, machine.Pin.OUT)
led_verde = machine.Pin(26, machine.Pin.OUT)

i2c = machine.I2C(0, scl=machine.Pin(22), sda=machine.Pin(21))

botao_1 = machine.Pin(12, machine.Pin.IN, machine.Pin.PULL_UP)
botao_2 = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_UP)

oled_width = 128
oled_height = 64
oled = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c)

while True:
    if botao_1.value() == 0:
        oled.fill(0)
        oled.text('A temperatura', 0, 10)
        oled.text('do quarto e:', 0, 20)
        oled.text('30 graus', 0, 30)  
        oled.show()  

    if botao_2.value() == 0:
        oled.fill(0)
        oled.text('A umidade', 0, 10)
        oled.text('da sala e:', 0, 20)
        oled.text('20', 0, 30)  
        oled.show()  

    sleep(0.1)