#!/usr/bin/env python3
from time import sleep
import signal
import sys
import time
import RPi.GPIO as GPIO
from effect import Effect
from os import listdir
from os.path import isfile, join
from config_parser import *
from cava_run import *
from display import *

BUTTON_LEFT_DOWN_GPIO = 6
BUTTON_LEFT_UP_GPIO = 5
BUTTON_RIGHT_UP_GPIO = 16
BUTTON_RIGHT_DOWN_GPIO = 24

selected_effect = ()
effects = list()

source = "false"

def signal_handler(sig, frame):
    GPIO.cleanup()
    sys.exit(0)

def button_pressed_callback(channel):
    print("Button pressed!")
    #print(channel)
    if(channel == 5):
      switch_source();

def switch_source():
   global source
   if(source == "true"):
     source = "false";
   else:
     source = "true"
   parse_config_file(source, selected_effect.channels, selected_effect.bars, selected_effect.size, selected_effect.freq)
   start_effect(selected_effect.file)

def parse_effects():
    global selected_effect
    path = "./effects/"
    files = [f for f in listdir(path) if isfile(join(path, f))]
    counter = 0
    for effect in files:
      if(effect == "ledbase.py"):
        continue
      effect_info = effect[:-3].split("_")
      effect_object = Effect(counter, effect, effect_info[0], effect_info[1], int(effect_info[2]), int(effect_info[3]), int(effect_info[4]))
      effects.append(effect_object)
      selected_effect = effect_object
      counter = counter + 1

if __name__ == '__main__':
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(BUTTON_LEFT_DOWN_GPIO, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(BUTTON_LEFT_UP_GPIO, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(BUTTON_RIGHT_UP_GPIO, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(BUTTON_RIGHT_DOWN_GPIO, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    GPIO.add_event_detect(BUTTON_LEFT_DOWN_GPIO, GPIO.FALLING, 
            callback=button_pressed_callback, bouncetime=200)
    GPIO.add_event_detect(BUTTON_LEFT_UP_GPIO, GPIO.FALLING,
            callback=button_pressed_callback, bouncetime=200)
    GPIO.add_event_detect(BUTTON_RIGHT_DOWN_GPIO, GPIO.FALLING,
            callback=button_pressed_callback, bouncetime=200)
    GPIO.add_event_detect(BUTTON_RIGHT_UP_GPIO, GPIO.FALLING,
            callback=button_pressed_callback, bouncetime=200)

    parse_effects()
    selected_effect = effects[2]
    parse_config_file(source, selected_effect.channels, selected_effect.bars, selected_effect.size, selected_effect.freq)
    
    start_effect(selected_effect.file)

    while(True):
     display(selected_effect.name, source)
     sleep(1.0 / 10)

    #signal.signal(signal.SIGINT, signal_handler)
    #signal.pause()
