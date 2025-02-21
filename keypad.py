import RPi.GPIO as GPIO
import time

class Keypad:
    def __init__(self, row_pins, col_pins):
        self.row_pins = row_pins
        self.col_pins = col_pins
        self.setup_gpio()
        
        self.keymap = [
            ['1', '2', '3'],
            ['4', '5', '6'],
            ['7', '8', '9'],
            ['*', '0', '#']
        ]

    def setup_gpio(self):
        GPIO.setmode(GPIO.BCM)
        
        for row in self.row_pins:
            GPIO.setup(row, GPIO.OUT)
            GPIO.output(row, GPIO.HIGH)
            
        for col in self.col_pins:
            GPIO.setup(col, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    def get_key(self):
        for i, row in enumerate(self.row_pins):
            GPIO.output(row, GPIO.LOW)
            
            for j, col in enumerate(self.col_pins):
                if GPIO.input(col) == GPIO.LOW:
                    time.sleep(0.02)  # Debounce
                    return self.keymap[i][j]
            
            GPIO.output(row, GPIO.HIGH)
        
        return None