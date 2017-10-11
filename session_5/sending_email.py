import requests
from flask import Flask, render_template, request
app = Flask("MyApp")


@app.route("/")
def hello_someone():
    return render_template("emailform.html")

@app.route("/signup", methods=["POST"])
def signup():
    form_data = request.form
    email = form_data["email"]
    first = form_data["first_name"]
    second = form_data["second_name"]
    send_simple_message(email, first, second)
    return "you have signed up as {} ".format(email)

def send_simple_message(email, first, second):
    return requests.post(
        "https://api.mailgun.net/v3/sandboxa506192b06074cb1bec955c3c6b08c0f.mailgun.org/messages",
        auth=("api", "key-b8f6655ee28db779a9e6ad1307a17b4c"),
        data={"from": "Excited User <mailgun@sandboxa506192b06074cb1bec955c3c6b08c0f.mailgun.org>",
              "to": [email],
              "subject": "Hello",
              "text": "Hello " + first + " " + second + "!"})




app.run(debug=True)
