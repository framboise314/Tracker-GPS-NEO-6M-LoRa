# install_pico_02
# Programme pour tester si les données GPS arrivent sur le port GP5
# et les afficher dans la console.
# d'après http://electroniqueamateur.blogspot.com/2021/08/module-gps-neo-6mv2-et-raspberry-pi-pico.html

from machine import Pin, UART
import utime, time
gps = UART(1, baudrate=9600, tx=Pin(4), rx=Pin(5))
 
while True:
    if gps.any():  # si nous avons reçu quelque chose...
        print(gps.readline().decode('utf-8'))  # noud affichons le message reçu
    time.sleep(0.5)  
