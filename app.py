from distutils.log import debug
from flask import Flask, render_template

# Flask Convention
app = Flask(__name__)

# Main page
@app.route("/")
def index():
    return render_template("index.html")

# TODO: Not sure this is required, interested to see how debugging works on render
# looks like debugger is on only if run with python3 app.py (instead of flask run)
if __name__ == "__main__":
    app.run(debug=True)