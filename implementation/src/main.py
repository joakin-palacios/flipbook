from machine import ADC, Pin, PWM
import uasyncio
# import motor_control as mtrc
# import neopixels_control as neopc
# import potentiometer_control as potc
import neopixel
import time
import _thread
import sys

wait=0.0001
adc_value=0

async def ledctrl():
    global wait
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    
    np = neopixel.NeoPixel(Pin(16), 9) # 10 cuz of nr of leds
    while True:
        np.fill(BLACK)
        np.write()
        await uasyncio.sleep(wait)
        np.fill(WHITE)
        np.write()
        await uasyncio.sleep(wait)
        
async def readingpots():
    global wait, adc_value
    
    pot = ADC(Pin(26))
    alpha=0.2
    filtered_value= 1
    
    while True:
        raw=pot.read_u16()
        filtered_value = alpha * raw + (1 - alpha) * filtered_value
        
        adc_value = int(filtered_value)       
        await uasyncio.sleep_ms(500)
    
async def pwmctrl():
    global adc_value
    
    pwm = PWM(Pin(22))
    pwm.freq(10000)  
    
    while True:
         pwm.duty_u16(adc_value)
         await uasyncio.sleep_ms(500)

# def wait_for_input():
#     
#     global wait
#     try:
#         wait = int(input("Please set a strobe wait time"))
#     except:
#         pass

async def main():
    global wait, adc_value

    led_control = uasyncio.create_task(ledctrl())
    pot_reading = uasyncio.create_task(readingpots())
    pwm_control = uasyncio.create_task(pwmctrl())


    while True:
        
        await uasyncio.sleep(1)
        print ("wait=",wait)
        print ("pmw_pot=",adc_value)

# _thread.start_new_thread(wait_for_input, ())
try:
    uasyncio.run(main())
finally:
    uasyncio.new_event_loop()
    

