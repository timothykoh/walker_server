from flask import Flask
from flask_sockets import Sockets
app = Flask(__name__)
sockets = Sockets(app)

@app.route("/<a>")
def hello(a):
    return "Hello World!" + a

@sockets.route("/echo")
def echo_socket(ws):
	while True:
		message = ws.receive()
		print message
		ws.send(message)

if __name__ == "__main__":
    app.run(debug=True)