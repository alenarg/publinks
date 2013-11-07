from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template('index.html', person=request.args.get('person'))

if __name__ == "__main__":
    app.run()