from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def hello_world():
    return '<h1>Hello World!</h1>'

@app.route("/identity", methods=["GET"])
def identity():
    return request.args.get("text")


if __name__ == '__main__':
    app.run()
