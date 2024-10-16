from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/gambling-behaviour")
def gambling_behaviour():
    return render_template('gambling-behaviour.html')

@app.route("/financial-exploitations")
def financial_exploitations():
    return render_template('financial-exploitations.html')

@app.route("/mental-health")
def mental_health():
    return render_template('mental-health.html')

if __name__ == "__main__":
    app.run(port=5000, debug=True)
