from flask import Flask

app=Flask(__name__)

@app.route("/index")
def hello_world():
    return "<p>Hello world</p>"
