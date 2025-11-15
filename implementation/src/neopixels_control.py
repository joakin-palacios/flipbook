from machine import Pin
import neopixel
import time

class Led_lights_values():
    def time_between_events(freq_hz):
        if freq_hz <= 0:
            freq_hz = 1
        return 1.0 / freq_hz

    color = (0, 0, 0)
    sleep_freq = 39

leds = Led_lights_values()


#         
#             vars.old_adc3 = vars.adc3
#             freq = 36 + (vars.old_adc3 / 65536) * (46 - 36)
#             vars.t_freq = time_between_events(freq)

def map_adc_ledcolors(value):
    outputs = [
    (0, 0, 0),         # BLACK
    (255, 0, 0),       # RED
    (255, 255, 0),     # YELLOW
    (0, 255, 0),       # GREEN
    (0, 255, 255),     # CYAN
    (0, 0, 255),       # BLUE
    (180, 0, 255),     # PURPLE
    (255, 100, 0),     # ORANGE
    (255, 0, 255),     # MAGENTA
    (139, 69, 19),     # BROWN
    (255, 255, 255)    # WHITE
    ]
    num_bins = len(outputs) # 11 
    bin_size = (2**16) / num_bins 

    index = int(value // bin_size)
    # Clamp index to avoid out-of-range error at the upper boundary
    index = min(index, num_bins - 1)

    return outputs[index]        

    
def process_pwm_value(in_value):
    if not (0 <= in_value <= 2**16):
        raise ValueError("Input must be between 0 and 65536")

    outputs = [-1, -0.1, -0.02, 0, 0.02, 0.1, 1]
    num_bins = len(outputs) # 7 
    bin_size = (2**16) / num_bins # =9362.14

    index = int(in_value // bin_size)
    # Clamp index to avoid out-of-range error at the upper boundary
    index = min(index, num_bins - 1)

    return outputs[index]    

def ledctrl():
    np = neopixel.NeoPixel(Pin(18), 9)
    BLACK = (0, 0, 0)
    while True:
        np.fill(leds.color)
        np.write()
#         time.sleep(0.000001)
        np.fill(BLACK)
        np.write()
        time.sleep(1/leds.sleep_freq)
    return

def change_led_freq(led_freq_adc):

    leds.sleep_freq = leds.sleep_freq + process_pwm_value(led_freq_adc)
    
        
        
def change_led_color (led_color_adc):
    leds.color = map_adc_ledcolors(led_color_adc)
    