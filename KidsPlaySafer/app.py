from flask import Flask, render_template, redirect, request, url_for


app = Flask(__name__)

@app.route("/")
def index():
    return url_for("index")

if __name__ == "__main__":
    app.run(port=1, debug=True)