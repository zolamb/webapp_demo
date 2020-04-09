'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Date: 04/11/20
File: webapp.py

Description:
    A simple webapp design using the Flask web framework. SMS receiving capabilities are handled
    through Twilio and allow users to interact with the WS2812B LED strip connected to the hosting
    Raspberry Pi.

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

#### Imports ######################################################################################
from flask import Flask, request								# For handling a local http server
from twilio.twiml.messaging_response import MessagingResponse   # Handles sending SMS messages but
																# not neccessary in this case


#### Globals ######################################################################################
app = Flask(__name__)	# Flask() object to handle the http server options


#### Function Definitions #########################################################################
@app.route("/") 		# Function decorator - Connects '/' endpoint to the 'hello_world()'
def hello_world():
	return "Hello World!"

@app.route("/sms", methods=['POST'])	# This route allows POST method to the specified endpoint
										# which is neccessary for receiving SMS data
def handle_text():
    phone_number = request.form['From']
    message_body = request.form['Body']
    print("\n\033[1;34m[+] ***-***-" + phone_number[-4:] + "\033[0m >> " + message_body)
    led_control.send_command(message_body)
    return ""


#### Main #########################################################################################
if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000') # Starts the local http server listening on port 5000

