from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome to my world /n consisitency is the key of succes🚀"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
