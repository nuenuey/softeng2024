from markupsafe import escape
from flask import Flask, request


app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello World!'


@app.route("/hello/<name>")
def say_hello(name):
    return f"안녕하세요! {escape(name)}님."

@app.route("/dan/<dan>")
def gugudan_html(dan):
    html_str =""
    for j in range(1, 10):
        html_str += f"{dan} X {j}= {int(dan) * j}<br>"
    return html_str


@app.route("/gugudan/")
def gugudan_arg_html():
    dan = request.args.get("dan", "2")
    html_str =""
    for j in range(1, 10):
        html_str += f"{dan} X {j}= <strong>{int(dan) * j}</strong><br>"
    return html_str

app.run(debug=True)