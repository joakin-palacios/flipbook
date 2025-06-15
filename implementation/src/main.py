from machine import ADC, Pin, PWM
import neopixel
import time

wait=0.0001
adc_value=0

def ledctrl():
    def time_between_events(freq_hz):
        """
        Calculate the time to wait between events at a given frequency.

        :param freq_hz: Frequency in Hertz (Hz)
        :return: Time between events in seconds
        """
        if freq_hz <= 0:
            raise ValueError("Frequency must be greater than zero.")
        return 1.0 / freq_hz
    global wait
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    
    np = neopixel.NeoPixel(Pin(1), 9) # 10 cuz of nr of leds
    while True:
        np.fill(WHITE)
        np.write()
        time.sleep(0.000001)
        np.fill(BLACK)
        np.write()
        time.sleep(time_between_events(41))
        
    
def pwmctrl(value):    
    pwm = PWM(Pin(0))
    pwm.freq(10000)  
    pwm.duty_u16(value)
    
 
pwmctrl(59626)
ledctrl()