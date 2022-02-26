from flask import Flask, render_template, request
import requests
import os
from twilio.rest import Client


app = Flask(__name__)



@app.route('/')
def index():
    return render_template('index.html')


@app.route('/send' , methods=["POST"])
def send_message():

    print("Sending message")
    number = request.form["tel-input"]
    print(number)

    #Adding a simple message
    message = "I Love you bebe !! - Paco"
    number = "+19252340221"
    print(f"message: {message}")
    #make the request

    #read about securing tokens in environment variables:
    # https://www.twilio.com/docs/usage/secure-credentials

    
    twilio_acct_id = os.environ['TWILIO_ACCT_ID']
    twilio_phone_number = os.environ['TWILIO_PHONE_NUMBER']
    twilio_auth_token = os.environ['TWILIO_AUTH_TOKEN']

    client = Client(twilio_acct_id, twilio_auth_token)

    message = client.messages.create(
        to= number, 
        from_= twilio_phone_number,
        body= message)

    print(f"Message id:  {message.sid}")
  

    data = {

        "success": "Message Sent!!"
    }
    return render_template("index.html", data=data)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')