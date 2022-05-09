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


proc = subprocess.Popen(['cava','-p' 'config'],stdout=subprocess.PIPE)
#strip = PixelStrip(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BR>
#strip.begin()
for line in io.TextIOWrapper(proc.stdout, encoding="utf-8"):
 singleBar = line[:-2].split(";")
 desired_array = [int(single) for single in singleBar]
 barCount = 0
 for i in range(strip.numPixels()):
  strip.setPixelColor(i, 0)
 for bar in desired_array:
  xypixel = pixel(barCount, bar)
  strip.setPixelColor(xypixel, Color(250,255,255))
  #print(xypixel)
  barCount = barCount + 1
 strip.show()
 #print("update")
