import sys

class recomputer_r110x(object):
    
    STA_LED_GREEN_BRIGHTNESS = "/sys/class/leds/led-green/brightness"
    STA_LED_RED_BRIGHTNESS = "/sys/class/leds/led-red/brightness"
    STA_LED_BLUE_BRIGHTNESS = "/sys/class/leds/led-blue/brightness"

    BUZZER_GPIO_CHIP = 'gpiochip2'
    BUZZER_GPIO_LINE = 9

    STA_LED_DIR = "/sys/class/leds"