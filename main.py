from flask import Flask, render_template
from flask_bootstrap import Bootstrap5
from flask_ckeditor import CKEditor
import os
import datetime


app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get("FLASK_KEY")
ckeditor = CKEditor(app)
Bootstrap5(app)


@app.route("/")
def homepage():
    year = datetime.date.today().year
    return render_template("index.html", year=year)


if __name__ == "__main__":
    app.run(debug=True, port=5001)
