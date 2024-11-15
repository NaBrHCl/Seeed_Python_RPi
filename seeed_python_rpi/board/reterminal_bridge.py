import sys

class reterminal_bridge(object):
    
    STA_LED_GREEN_BRIGHTNESS = "/sys/class/leds/usr_led2/brightness"
    STA_LED_RED_BRIGHTNESS = "/sys/class/leds/usr_led1/brightness"
    USR_LED_0_BRIGHTNESS = "/sys/class/leds/usr_led0/brightness"

    BUZZER_BRIGHTNESS = "/sys/class/leds/usr_buzzer/brightness"
    LIGHT_ILLUMINANCE = "/sys/bus/iio/devices/iio:device0/in_illuminance_input"

    EVENT_CLASS_PATH = "/sys/class/input/event"
    EVENT_DEVICE_PATH = "/dev/input/event"
    BUTTON_DEVICE_NAME = "gpio_keys"
    ACCELERATION_DEVICE_NAME = "ST LIS3LV02DL Accelerometer"

    FAN_GPIO_CHIP = 'gpiochip0'
    FAN_GPIO_line = 23

    # because of the hardware limitation,we can only use one of rs232 or rs485 at a certain time. 
    RS232_OR_RS485 = "None" 
    RS232_OR_RS485_SWITCH_GPIO_CHIP = 'gpiochip0'
    RS232_OR_RS485_SWITCH_GPIO_LINE = 25

    RS485_TX_RX_STAT = "None" 
    RS485_TX_RX_SWITCH_GPIO_CHIP = 'gpiochip0'
    RS485_TX_RX_SWITCH_GPIO_LINE = 17

    STA_LED_DIR = "/sys/class/leds"