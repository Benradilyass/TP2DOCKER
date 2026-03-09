from flask import Flask
app = Flask(_name_)
@app.route("/")
def home():
    return "Hello DevOps - Docker CI Pipeline!"
if _name_=="_main_":
    app.run(host="0.0.0.O", port=5000)