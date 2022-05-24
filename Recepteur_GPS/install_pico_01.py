# Programme pour tester si l'installation de MicroPython est correcte
# et si on peut afficher des infos sur l'écran
import st7789

WIDTH = 240
HEIGHT = 240

display = st7789.ST7789(WIDTH, HEIGHT, rotate180=False)

display.set_pen(0, 255, 0)                    # change the pen colour
display.text("Hello World",5,5,240,2)                    # display some text on the screen
display.update()                              # update the display
