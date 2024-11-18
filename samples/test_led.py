#!/usr/bin/env python3

import seeed_python_rpi.core as rt
import time

try:
    get_led = rt.sta_led
    print("STA BLINK ")
    rt.sta_led = True
    time.sleep(1)
    rt.sta_led = False
except:
    pass

try:
    get_led = rt.usr_led
    print("USR BLINK ")
    rt.usr_led = True
    time.sleep(1)
    rt.usr_led = False
except:
    pass
    
try:
    get_led = rt.sta_led_green
    print("STA GREEN BLINK ")
    rt.sta_led_green = True
    time.sleep(1)
    rt.sta_led_green = False
except:
    pass
    
try:
    get_led = rt.sta_led_red
    print("STA RED BLINK ")
    rt.sta_led_red = True
    time.sleep(1)
    rt.sta_led_red = False
except:
    pass
    
try:
    get_led = rt.sta_led_blue
    print("STA BLUE BLINK ")
    rt.sta_led_blue = True
    time.sleep(1)
    rt.sta_led_blue = False
except:
    pass