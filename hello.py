from flask import Flask
from flask import render_template
from flask import request
import models

app = Flask(__name__)


@app.route("/")
def hello():
    return render_template(
    	'index.html',
        articles=models.articles,
    )

@app.route("/about")
def about():
    return render_template('about.html')


if __name__ == "__main__":
    app.run(debug=True)
