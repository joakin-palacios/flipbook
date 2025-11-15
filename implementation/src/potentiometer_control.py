from machine import ADC, Pin
import motor_control
import neopixels_control
 
class Potentiometer_values():
    motor_adc          = 59626
    led_freq_adc       = 59626
    led_color_adc      = 59626
    last_motor_adc     = 59626
    last_led_freq_adc  = 59626
    last_led_color_adc = 59626

pots = Potentiometer_values()

def init_pots():
    pot1 = ADC(Pin(26)) 
    pot2 = ADC(Pin(27))
    pot3 = ADC(Pin(28))
    return pot1, pot2, pot3

def read_pots(pot1, pot2, pot3):
    pots.motor_adc = pot1.read_u16()
    pots.led_freq_adc   = pot2.read_u16()
    pots.led_color_adc = pot3.read_u16()
    return

def process_pots():
    
    def change_detected(new, old, NOISE=500):
        return abs(new - old) >= NOISE
    
    if change_detected(pots.motor_adc, pots.last_motor_adc):
        pots.last_motor_adc = pots.motor_adc

    if change_detected(pots.led_freq_adc, pots.last_led_freq_adc):
        pots.last_led_freq_adc = pots.led_freq_adc

    if change_detected(pots.led_color_adc, pots.last_led_color_adc):
        pots.last_led_color_adc = pots.led_color_adc
    return