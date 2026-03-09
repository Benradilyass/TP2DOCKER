from flask import Flask

app = Flask(__name__)  # use double underscores

@app.route("/")
def home():
    return "Hello DevOps - Docker CI Pipeline!"

if __name__ == "__main__":  # use double underscores
    app.run(host="0.0.0.0", port=5000)  # 0, not O