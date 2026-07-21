from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chickens")
@app.route("/gohyanchengdarriuswuyancheng")
def chicken():
    return render_template("chickens.html")

@app.route("/pandas")
def panda():
    return render_template("pandas.html")

@app.route("/presidents")
def president():
    return render_template("presidents.html")

if __name__ == "__main__":
    app.run(port=5678)

