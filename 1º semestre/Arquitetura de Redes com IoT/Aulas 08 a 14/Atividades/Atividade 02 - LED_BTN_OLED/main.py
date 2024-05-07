import time
import machine
import ssd1306

# Botões de Navegação
btn_baixo = machine.Pin(26, machine.Pin.IN, machine.Pin.PULL_UP)
btn_cima = machine.Pin(27, machine.Pin.IN, machine.Pin.PULL_UP)

# Botões de ON e OFF
btn_on = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_UP)
btn_off = machine.Pin(12, machine.Pin.IN, machine.Pin.PULL_UP)

# LEDs
led_ligado = machine.Pin(18, machine.Pin.OUT)
led_desligado = machine.Pin(17, machine.Pin.OUT)

largura = 128
altura = 64
i2c = machine.I2C(0, scl=machine.Pin(22), sda=machine.Pin(21))
tela = ssd1306.SSD1306_I2C(largura, altura, i2c)

qual_tela = 1
status_iluminacao = "OFF"
status_ar_condicionado = "OFF"
status_portao_principal = "OFF"
status_cameras = "OFF"


led_desligado.value(1)
led_ligado.value(0)


def tela_iluminacao():
    global status_iluminacao    
    tela.fill(0)
    tela.text("ILUMINACAO", 0, 0)
    if status_iluminacao == "OFF":
      tela.text("Status:  OFF", 0, 25)
      led_ligado.value(0)
      led_desligado.value(1)
    elif status_iluminacao == "ON":
      tela.text("Status:  ON", 0, 25)
      led_ligado.value(1)
      led_desligado.value(0)
    
    tela.text("[1/4]", 0, 50)
    tela.show()

    if btn_on.value() == 0:
        status_iluminacao = "ON"
    if btn_off.value() == 0:
        status_iluminacao = "OFF"

def tela_ar_condicionado():
    global status_ar_condicionado
    tela.fill(0)
    tela.text("AR CONDICIONADO", 0, 0)
    if status_ar_condicionado == "OFF":
      tela.text("Status:  OFF", 0, 25)
      led_ligado.value(0)
      led_desligado.value(1)
    elif status_ar_condicionado == "ON":
      tela.text("Status:  ON", 0, 25)
      led_ligado.value(1)
      led_desligado.value(0)
    
    tela.text("[2/4]", 0, 50)
    tela.show()

    if btn_on.value() == 0:
        status_ar_condicionado = "ON"
    if btn_off.value() == 0:
        status_ar_condicionado = "OFF"

def tela_portao_principal():
    global status_portao_principal
    tela.fill(0)
    tela.text("PORTAO PRINC.", 0, 0)
    if status_portao_principal == "OFF":
      tela.text("Status:  OFF", 0, 25)
      led_ligado.value(0)
      led_desligado.value(1)
    elif status_portao_principal == "ON":
      tela.text("Status:  ON", 0, 25)
      led_ligado.value(1)
      led_desligado.value(0)
    
    tela.text("[3/4]", 0, 50)
    tela.show()

    if btn_on.value() == 0:
        status_portao_principal = "ON"
    if btn_off.value() == 0:
        status_portao_principal = "OFF"

def tela_cameras():
    global status_cameras
    tela.fill(0)
    tela.text("CAMERAS", 0, 0)
    if status_cameras == "OFF":
      tela.text("Status:  OFF", 0, 25)
      led_ligado.value(0)
      led_desligado.value(1)
    elif status_cameras == "ON":
      tela.text("Status:  ON", 0, 25)
      led_ligado.value(1)
      led_desligado.value(0)
    
    tela.text("[4/4]", 0, 50)
    tela.show()

    if btn_on.value() == 0:
        status_cameras = "ON"
    if btn_off.value() == 0:
        status_cameras = "OFF"

while True:
    if btn_baixo.value() == 0 and qual_tela <= 3 :
        #print("Botão Baixo foi pressionado - valor:", qual_tela)
        qual_tela += 1
    if btn_cima.value() == 0 and qual_tela > 1 :
        #print("Botão Cima foi pressionado - valor:", qual_tela)
        qual_tela -= 1
    

    if qual_tela == 1:
        tela_iluminacao()
            
    elif qual_tela == 2:
        tela_ar_condicionado()

    elif qual_tela == 3:
        tela_portao_principal()

    elif qual_tela == 4:
        tela_cameras()

    time.sleep(0.1)