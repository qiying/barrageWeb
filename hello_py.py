from flask import Flask
app = Flask(__name__)

@app.route("/")
#def index():
#	return "<h1>Hello world</h1>"
def hello():
    return "Hello World!"

@app.route("/error")
def error():
	raise RuntimeError
	
if __name__ == "__main__":
    app.run(debug=True)
