import _thread
import time
import motor_control 
import neopixels_control 
import potentiometer_control
DEBUG=True 

def main():
    pot1, pot2, pot3 = potentiometer_control.init_pots()
    pwm = motor_control.pwm_init()
    _thread.start_new_thread(neopixels_control.ledctrl,())

    while True:
        potentiometer_control.read_pots(pot1, pot2, pot3)
        potentiometer_control.process_pots()
        motor_control.pwmctrl(pwm, potentiometer_control.pots.last_motor_adc)
        neopixels_control.change_led_freq(potentiometer_control.pots.last_led_freq_adc)
        neopixels_control.change_led_color(potentiometer_control.pots.last_led_color_adc)
        if DEBUG:
            print (f'''
Color: {neopixels_control.leds.color} Led_ADC: {potentiometer_control.pots.last_led_color_adc}
Frequency: {neopixels_control.leds.sleep_freq} Frequency_ADC: {potentiometer_control.pots.last_led_freq_adc}
Motor_PMW: {motor_control.current_pwm_value} PMW_ADC: {potentiometer_control.pots.last_motor_adc}
''')
        time.sleep(0.5)
        
        

if __name__ == "__main__":
    main()
