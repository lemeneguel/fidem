from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def index():
    return 'Hello World!'

@app.route("/form/<name>")
def form(name):
    return render_template("form.html", name=name)

@app.route("/shopping")
def shopping():
    food = ["Cheese", "Tuna", "Beef"]
    return render_template("shopping.html", food=food)

if __name__ == "__main__":
    app.run()