import sys

class reterminal_plus(object):
    
    USR_LED_0_BRIGHTNESS = "/sys/class/leds/usr-led/brightness"
    BUZZER_BRIGHTNESS = "/sys/class/leds/usr_buzzer/brightness"
    LIGHT_ILLUMINANCE = "/sys/bus/iio/devices/iio:device0/in_illuminance_input"

    EVENT_CLASS_PATH = "/sys/class/input/event"
    EVENT_DEVICE_PATH = "/dev/input/event"
    BUTTON_DEVICE_NAME = "gpio_keys"

    STA_LED_DIR = "/sys/class/leds"