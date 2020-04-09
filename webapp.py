'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Date: 04/11/20
File: webapp.py

Description:
    A simple webapp design using the Flask web framework. SMS receiving capabilities are handled
    through Twilio and allow users to interact with the WS2812B LED strip connected to the hosting
    Raspberry Pi.

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

#### Imports ######################################################################################
from flask import Flask, request								# Starts and handles an http server
from twilio.twiml.messaging_response import MessagingResponse   # Handles SMS messaging


#### Globals ######################################################################################
app = Flask(__name__)	# Flask() object that lets you start the http server and specify endpoints


#### Function Definitions #########################################################################
@app.route("/") 		# Function decorator - Connects '/' endpoint to the 'hello_world()'
def hello_world():
	return "Hello World!"

@app.route("/sms") 		# Function decorator - Connects '/sms' endpoint to 'handle_text()'
def handle_text():
    return "Text Recieved"


#### Main #########################################################################################
if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000') # Starts the local http server listening on port 5000

