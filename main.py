from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
@app.route("/form/<name>")
def form(name):
    return render_template("form.html", name=name)

if __name__ == "__main__":
    app.run()