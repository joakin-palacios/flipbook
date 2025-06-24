from machine import ADC, Pin, PWM
import neopixel
import time
import _thread

class global_values:
    def __init__(self):
        self.adc1 = 59626
        self.adc2 = 59626
        self.adc3 = 59626
        self.old_adc1 = 59626
        self.old_adc2 = 59626
        self.old_adc3 = 59626
        self.t_freq = time_between_events(41)
        


def time_between_events(freq_hz):
        if freq_hz <= 0:
            raise ValueError("Frequency must be greater than zero.")
        return 1.0 / freq_hz
    
def ledctrl():
    global vars
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)   
    np = neopixel.NeoPixel(Pin(18), 9) # 10 cuz of nr of leds
    vars.t_freq=time_between_events(41)
    while True:
        np.fill(WHITE)
        np.write()
        time.sleep(0.000001)
        np.fill(BLACK)
        np.write()
        time.sleep(vars.t_freq)
        
    
def pwm_init():
    global pwm
    pwm = PWM(Pin(21))
    pwm.freq(10000)
    
def pwmctrl(value):
    global pwm
    pwm.duty_u16(value)

def readingpots():
    global pot, pot2, pot3, vars
    vars.adc1 = pot.read_u16()  # Returns value between 0 and 65535
    vars.adc2 = pot2.read_u16()  # Returns value between 0 and 65535
    vars.adc3 = pot3.read_u16()  # Returns value between 0 and 65535
    print("ADC 0:", vars.adc1,"ADC 1:", vars.adc2,"ADC 2:", vars.adc3 )
 

def initpots():
    global pot, pot2, pot3
    pot = ADC(Pin(26))  # GP26 is ADC0
    pot2 = ADC(Pin(27))  # GP26 is ADC0
    pot3 = ADC(Pin(28))  # GP26 is ADC0

        
def change_detected(new, old, threshold = 1000):
    change = abs(new - old)
    if change >= threshold:
        return True
    return False


def main():
    global vars
    #set up
    _thread.start_new_thread(ledctrl, ())
    pwm_init()
    initpots()
    pwmctrl(vars.old_adc1)
    
    #loop
    while True:
        readingpots()
        time.sleep(0.5)
        if change_detected(vars.adc1, vars.old_adc1):
            vars.old_adc1 = vars.adc1
            print("change in pot 1 detected")
        if change_detected(vars.adc2, vars.old_adc2):
            vars.old_adc2 = vars.adc2
            print("change in pot 2 detected")
        if change_detected(vars.adc3, vars.old_adc3):
            vars.old_adc3 = vars.adc3
            print("change in pot 3 detected")
            
vars = global_values()
main()