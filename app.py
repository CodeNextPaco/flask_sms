from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/send' , methods=["POST"])
def send_message():

    print("Sending message")
    number = request.form["tel-input"]
    print(number)



    data = {

        "success": "Message Sent"
    }
    return render_template("index.html", data=data)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')