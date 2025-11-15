from machine import PWM, Pin
current_pwm_value = 29626

def pwm_init():
    pwm = PWM(Pin(21))
    pwm.freq(10000)
    return pwm

def pwmctrl(pwm, value):
    global current_pwm_value
    
    def change_pwm_value(in_value):
        if not (0 <= in_value <= 2**16):
            raise ValueError("Input must be between 0 and 65536")

        outputs = [-1000, -500, -100, 0, 100, 500, 1000]
        num_bins = len(outputs) # 7 
        bin_size = (2**16) / num_bins # =9362.14

        index = int(in_value // bin_size)
        # Clamp index to avoid out-of-range error at the upper boundary
        index = min(index, num_bins - 1)

        return outputs[index]
    
    current_pwm_value = current_pwm_value + change_pwm_value(value)
    if current_pwm_value < 0:
        current_pwm_value = 0
    elif current_pwm_value > 65535:
        current_pwm_value = 65535
        
    pwm.duty_u16(current_pwm_value)