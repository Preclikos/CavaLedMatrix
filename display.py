from ST7789 import ST7789
from colorsys import hsv_to_rgb
from PIL import Image, ImageDraw, ImageFont
import time
SPI_SPEED_MHZ = 80

# Give us an image buffer to draw into
#image = Image.new("RGB", (240, 240), (0, 0, 0))
#draw = ImageDraw.Draw(image)

# Standard display setup for Pirate Audio, except we omit the backlight pin
st7789 = ST7789(
    rotation=90,     # Needed to display the right way up on Pirate Audio
    port=0,          # SPI port
    cs=1,            # SPI port Chip-select channel
    dc=9,            # BCM pin used for data/command
    backlight=13,  # We'll control the backlight ourselves
    spi_speed_hz=SPI_SPEED_MHZ * 1000 * 1000
)

dot_color = (254,254,0)

font = ImageFont.truetype("agane65bold.ttf", 24)
font_small = ImageFont.truetype("agane65bold.ttf", 18)

width = 240
height = 240
h_width = width / 2
h_height = height / 2

def draw_dots(draw):
  draw.rectangle((0, 50, 15, 65), dot_color)
  draw.rectangle((0, 185, 15, 200), dot_color)
  draw.rectangle((225, 50, 240, 65), dot_color)
  draw.rectangle((225, 185, 240, 200), dot_color)
  #print(str(x) +" - "+str(y))
  #draw.text((x, y),"Sample Text",(r,g,b))
  draw.text((29, 49),"Source",(255,255,255),font=font)
  draw.text((170, 49),"Pair",(255,255,255),font=font)
  draw.text((29, 184),"Prev",(255,255,255),font=font)
  draw.text((160, 184),"Next",(255,255,255),font=font)

def display(name, source):
  image = Image.new("RGB", (240, 240), (0, 0, 0))
  draw = ImageDraw.Draw(image)
  if(source == "true"):
    draw.text((29, 25),"External",(255,255,255),font=font_small)
  else:
    draw.text((29, 25),"Internal",(255,255,255),font=font_small)
  (x, y) = font.getsize(name)
  draw.text((h_width - (x / 2), (h_height - (y /2))),name,(255,255,255),font=font)
  draw_dots(draw)

  #hue = time.time() / 10
  #r, g, b = [int(c * 255) for c in hsv_to_rgb(hue, 1.0, 1.0)]
  #draw.rectangle((0, 0, 10, 10), (r, g, b))
  st7789.display(image)


