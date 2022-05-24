from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

"""
You can also set port/host as Environment variables 
by using <$ export PORT=500> <$export HOST=0.0.0.0>
"""
if __name__ == "__main__":
	app.run(port = 5000, host = "0.0.0.0")