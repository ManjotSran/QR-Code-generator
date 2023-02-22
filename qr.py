import os
import qrcode

img = qrcode.make('https://www.youtube.com/watch?v=K2aXGlCKiDU')
img.save("CS50W0.png", "PNG")
os.system("open CS50W0.png")