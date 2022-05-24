'''
Utilisation d'un module GPS NEO 6MV2 avec un
Raspberry Pi Pico.
Nous utilisons la bibliothèque micropyGPS (par inmcm) pour traiter les informations reçues.
Pour plus d'infos:
https://electroniqueamateur.blogspot.com/2021/08/module-gps-neo-6mv2-et-raspberry-pi-pico.html
'''
import machine
from utime import sleep
from micropyGPS import MicropyGPS  # https://github.com/inmcm/micropyGPS

uart= machine.UART(1,baudrate=9600)  # initialisation UART
gps = MicropyGPS() # création d'un objet GPS

while True:
    if uart.any():  # si nous avons reçu quelque chose...
        donnees_brutes = str(uart.readline())
        print(donnees_brutes)
        for x in donnees_brutes:
            #print(x)
            gps.update(x)

        print('Latitude: ' ,gps.latitude_string())
        print('Latitude (tuple): ' , gps.latitude)
        print('Longitude: ' ,gps.longitude_string())
        print('Longitude (tuple): ' , gps.longitude)
        print('Altitude: ' , gps.altitude)
        print('Vitesse: ', gps.speed_string('kph'))
        print('Date: ' , gps.date_string('s_dmy'))
        print('')

    sleep(.1)
