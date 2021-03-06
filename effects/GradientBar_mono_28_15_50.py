import io
import subprocess
import ledbase
from rpi_ws281x import Color, PixelStrip
from ledbase import *

#filters output
#strip = PixelStrip(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BR>
#strip.begin()
strip = PixelStrip(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
strip.begin()

color_gradients = linear_gradient("#448300", "#FF0000", n=16)

proc = subprocess.Popen(['cava','-p' 'configs/config'],stdout=subprocess.PIPE)
#strip = PixelStrip(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BR>
#strip.begin()
for line in io.TextIOWrapper(proc.stdout, encoding="utf-8"):
 singleBar = line[:-2].split(";")
 desired_array = [int(single) for single in singleBar]
 barCount = 0
 for i in range(0, strip.numPixels(), 1):
  strip.setPixelColor(i, Color(0, 0, 0))
 for bar in desired_array:
#  xypixel = pixel(barCount, 0)
#  strip.setPixelColor(xypixel, Color(250,0,0))
  for x in range(0, bar + 1):
   color = Color(color_gradients['r'][x], color_gradients['g'][x],color_gradients['b'][x])
   if(x == bar):
    xypixel = pixel(barCount, x)
    strip.setPixelColor(xypixel, color)
   else:
    if(x == 0):
     xypixel = pixel(barCount, x)
     strip.setPixelColor(xypixel, color)
    else:
     xypixel = pixel(barCount, x)
     strip.setPixelColor(xypixel, color)
  #print(xypixel)
  barCount = barCount + 1
 strip.show()
 #print("update")
