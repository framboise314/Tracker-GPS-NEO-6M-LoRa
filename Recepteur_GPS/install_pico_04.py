# install_pico_03
# Programme pour séparer les informations fournies par le GPS
# et les afficher dans la console et sur l'écran de la carte PICO EXPLORER
# Pour visualiser la LED PPS qui est sous la carte GPS
# La sortie PPS est reliée au GP0 et déclenche un Interruption
# sur front montant qui fait clignoter la LED de la carte PICO
# d'après http://electroniqueamateur.blogspot.com/2021/08/module-gps-neo-6mv2-et-raspberry-pi-pico.html

from machine import Pin, UART
from pimoroni import Button
from micropyGPS import MicropyGPS

import utime, time
# Gestionnaire d'écran
import st7789
# Dimensions de l'écran
WIDTH = 240
HEIGHT = 240
# Créer l'instance de l'écran
display = st7789.ST7789(WIDTH, HEIGHT, rotate180=False)

display.set_pen(0, 255, 0)                    # change the pen colour RVB => vert
display.text("Framboise314",5,5,240,2)         # display some text on the screen
display.update()                              # update the display
# test de l'écran, affiche Hello World 2 secondes puis efface l'écran
time.sleep(2)
display.set_pen(0, 0, 0)                    # change the pen colour RVB => vert
display.clear()                              # update the display
display.update()                              # update the display



uart = UART(1, baudrate=9600, tx=Pin(4), rx=Pin(5))  # Configure la liaison série
gps = MicropyGPS(2) # création d'un objet GPS


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
    # Effacer l'écran
    display.set_pen(0, 0, 0)                    # change the pen colour RVB => vert
    display.clear()                              # update the display
    display.update()                              # update the display
    
    if uart.any():  # si nous avons reçu quelque chose...
        donnees_brutes = str(uart.readline())
        # print(donnees_brutes)
        # Ce try permet d'éliminer l'erreur d'index qui se produit de temps en temps
        try:
            for x in range(0, len(donnees_brutes)):
            # print("X = ",x)
            # print("longueur :", len(donnees_brutes))
                gps.update(donnees_brutes[x])
        except IndexError:
            pass
        
        display.set_pen(0,255,255)
        print('Date: ' , gps.date_string('s_dmy'))
        display.text(gps.date_string('s_dmy'),5,25,240,2)
        
        heure = gps.timestamp[0]
        minutes = gps.timestamp[1]
        secondes = gps.timestamp[2]
        heure_affich = str(heure) + ":" + str(minutes) + ":" + str(secondes)
        display.text(heure_affich,120,25,240,2)
        
        print('Latitude: ' ,gps.latitude_string())
        print('latitude (tuple): ' , gps.latitude)
        display.text("Latitude",5,55,240,2)
        display.text(gps.latitude_string(),5,75,240,2)
        
        print('longitude (tuple): ' , gps.longitude)
        print('Longitude: ' ,gps.longitude_string())
        display.text("Longitude",5,105,240,2)
        display.text(gps.longitude_string(),5,125,240,2)

        print('Altitude: ' , gps.altitude)
        print('Vitesse: ', gps.speed_string('kph'))
        display.text("Altitude",5,155,240,2)
        display.text(str(gps.altitude),5,175,240,2)
        display.text("Vitesse",5,205,240,2)
        display.text(gps.speed_string('kph'),5,225,240,2)
        
        print("Satellites", gps.satellites_in_use)
        print("Heure", gps.timestamp)

        print('')
        display.update()

    time.sleep(1)
