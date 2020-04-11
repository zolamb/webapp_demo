'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Date: 04/09/20
File: webapp.py

Description:
    A simple webapp design using the Flask web framework. SMS receiving capabilities are handled
    through Twilio and allow users to interact with the WS2812B LED strip connected to the hosting
    Raspberry Pi.

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

#### Imports ######################################################################################
from led_control import LED_Control								# For handling LED strip commands
from flask import Flask, request								# For handling a local http server
import os


#### Globals ######################################################################################
app = Flask(__name__)	# Flask() object to handle the http server options
led_control = LED_Control()

#### Function Definitions #########################################################################
@app.route("/") 		# Function decorator - Connects '/' endpoint to the 'hello_world()'
def hello_world():
	return "Hello World!"

@app.route("/sms", methods=['POST'])	# This route allows POST method to the specified endpoint
										# which is neccessary for receiving SMS data
def handle_text():
    # Store relevant text message data
    phone_number = request.form['From']
    message_body = request.form['Body']
    
    # Interact with LED strip
    print("\n\033[1;34m[+] Webapp \033[0m\t>> Message from ***-***-" + phone_number[-4:] + ": \"" +
    	  message_body + "\"")
    led_control.send_command(message_body)
    return ""

def init_output():
    os.system("clear")
    print("\033[1;34m[+] Phone number: \033[0m(231)-333-9003")
    led_control.display_options()


#### Main #########################################################################################
if __name__ == "__main__":
    init_output()
    app.run(host='0.0.0.0', port='5000') # Starts the local http server listening on port 5000

