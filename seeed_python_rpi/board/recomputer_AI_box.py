import sys

class recomputer_AI_box(object):
    
    STA_LED_GREEN_BRIGHTNESS = "/sys/class/leds/usr-led/brightness"
    USR_LED_0_BRIGHTNESS = "/sys/class/leds/usr-led/brightness"

    FAN_GPIO_CHIP = 'gpiochip0'
    FAN_GPIO_LINE = 16

    STA_LED_DIR = "/sys/class/leds"