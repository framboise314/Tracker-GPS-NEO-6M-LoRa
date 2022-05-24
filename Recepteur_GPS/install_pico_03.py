# install_pico_03
# Programme pour tester si les données GPS arrivent sur le port GP5
# et les afficher dans la console.
# Pour visualiser la LED PPS qui est sous la carte GPS
# La sortie PPS est reliée au GP0 et déclenche un Interruption
# sur front montant qui fait clignoter la LED de la carte PICO
# d'après http://electroniqueamateur.blogspot.com/2021/08/module-gps-neo-6mv2-et-raspberry-pi-pico.html

from machine import Pin, UART
from pimoroni import Button

import utime, time

gps = UART(1, baudrate=9600, tx=Pin(4), rx=Pin(5))

# Allumer/Eteindre la LED du PICO
# Vérification du lancement du programme
led = Pin(25, Pin.OUT)
led.on()
time.sleep(0.5)
led.off()

# Déclarer le pps comme un bouton sur GP0
pps = Pin(0, Pin.IN, Pin.PULL_UP) 

# Interruption exécutée quand PPS passe à 1
def callback(pps):
    led.toggle()

pps.irq(trigger=Pin.IRQ_RISING, handler=callback)

while True:
    if gps.any():  # si nous avons reçu quelque chose...
        print(gps.readline().decode('utf-8'))  # noud affichons le message reçu
    time.sleep(0.5)  
