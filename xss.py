from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def home():
    name = request.args.get("name")
    return f"<h1>Hello {name}</h1>"   

print("hello"
