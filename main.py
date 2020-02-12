from flask import Flask, render_template
app = Flask(__name__)

@app.route("/form/<name>")
def profile(name):
    return render_template("form.html", name=name)

if __name__ == "__main__":
    app.run()