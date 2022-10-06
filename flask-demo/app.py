from flask import Flask

app = Flask(__name__)
app.config["JSON_AS_ASCII"] = False

@app.route('/hello/<s>')
def hello(s: str):
    pass


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080)
