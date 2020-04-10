'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Date: 04/09/20
File: led_control.py

Description:
    Controls the WS2812B LED strip connected to a Raspberry Pi. Allows for various LED effects.

Credit:
    Various LED effects and init have been taken from: https://github.com/jgarff/rpi_ws281x

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
 
#### Imports ######################################################################################
import time                 # Handles delay between individual LED signals
from neopixel import *      # Handles the WS2812B LED strip


#### Function Definitions #########################################################################
class LED_Control():
    def __init__(self):
        # LED strip configuration:
        LED_COUNT      = 16      # Number of LED pixels.
        LED_PIN        = 18      # GPIO pin connected to the pixels (18 uses PWM!).

        #LED_PIN        = 10      # GPIO pin connected to the pixels (10 uses SPI /dev/spidev0.0).
        LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
        LED_DMA        = 10      # DMA channel to use for generating signal (try 10)
        LED_BRIGHTNESS = 255     # Set to 0 for darkest and 255 for brightest
        LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)
        LED_CHANNEL    = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53

        # Create NeoPixel object with appropriate configuration.
        self.strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, 
                                        LED_BRIGHTNESS, LED_CHANNEL)
        
        # Intialize the library (must be called once before other functions).
        self.strip.begin()

        # List of commands
        self.clear_strip = "clear strip"
        self.rainbow_ = "rainbow"
        self.rainbow_cycle_ = "rainbow cycle"
        self.color_sweep_red = "sweep red"
        self.color_sweep_blue = "sweep blue"
        self.color_sweep_green = "sweep green"
        self.theater_chase_white = "theater chase white"
        self.theater_chase_red = "theater chase red"
        self.theater_chase_blue = "theater chase blue"

    def display_options(self):
        print('''\033[1;34m[+] Options:\033[0m
        1) sweep red
        2) sweep blue
        3) sweep green
        4) theater chase white
        5) theater chase red
        6) theater chase blue
        7) rainbow
        8) rainbow cycle
        
        "clear strip" to clear the strip
        ''')

    
    ''' send_command():
        @param1: string     - Command to perform on the LED strip
        @reutrn: string     - The successful command that was performed

        Description:
                This function is meant to interact with the webapp.py program
                in order to allow the body of messages recieved from Twilio
                to execute commands on the LED strip
    '''
    def send_command(self, command):
        command = command.lower().strip()
        if(command == self.clear_strip):
            self.color_sweep(self.strip, Color(0,0,0), 10)

        if(command == self.rainbow_):
            self.rainbow(self.strip)

        if(command == self.rainbow_cycle_):
            self.rainbow_cycle(self.strip)
        
        if(command == self.color_sweep_red):
            self.color_sweep(self.strip, Color(0, 255, 0))
        
        if(command == self.color_sweep_green):
            self.color_sweep(self.strip, Color(255, 0, 0))
        
        if(command == self.color_sweep_blue):
            self.color_sweep(self.strip, Color(0, 0, 255))
        
        if(command == self.theater_chase_white):
            self.theater_chase(self.strip, Color(127, 127, 127))
        
        if(command == self.theater_chase_red):
            self.theater_chase(self.strip, Color(0,   127,   0))
        
        if(command == self.theater_chase_blue):
            self.theater_chase(self.strip, Color(  0,   0, 127))

    # Define functions which animate LEDs in various ways.
    def color_sweep(self, strip, color, wait_ms=50):
        """Wipe color across display a pixel at a time."""
        for i in range(strip.numPixels()):
            strip.setPixelColor(i, color)
            strip.show()
            time.sleep(wait_ms/500.0)
     
    def theater_chase(self, strip, color, wait_ms=50, iterations=10):
        """Movie theater light style chaser animation."""
        for j in range(iterations):
            for q in range(3):
                for i in range(0, strip.numPixels(), 3):
                    strip.setPixelColor(i+q, color)
                strip.show()
                time.sleep(wait_ms/1000.0)
                for i in range(0, strip.numPixels(), 3):
                    strip.setPixelColor(i+q, 0)
     
    def wheel(self, pos):
        """Generate rainbow colors across 0-255 positions."""
        if pos < 85:
            return Color(pos * 3, 255 - pos * 3, 0)
        elif pos < 170:
            pos -= 85
            return Color(255 - pos * 3, 0, pos * 3)
        else:
            pos -= 170
            return Color(0, pos * 3, 255 - pos * 3)
     
    def rainbow(self, strip, wait_ms=20, iterations=1):
        """Draw rainbow that fades across all pixels at once."""
        for j in range(256*iterations):
            for i in range(strip.numPixels()):
                strip.setPixelColor(i, self.wheel((i+j) & 255))
            strip.show()
            time.sleep(wait_ms/1000.0)
     
    def rainbow_cycle(self, strip, wait_ms=20, iterations=5):
        """Draw rainbow that uniformly distributes itself across all pixels."""
        for j in range(256*iterations):
            for i in range(strip.numPixels()):
                strip.setPixelColor(i, self.wheel((int(i * 256 / strip.numPixels()) + j) & 255))
            strip.show()
            time.sleep(wait_ms/7500.0)
