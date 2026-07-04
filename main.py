from flask import Flask, render_template
from jinja2 import Template

app=Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")

# @app.route("/<name>/")
# def about(name):
#     return render_template("about.html",name=name)

@app.route("/api/v1/<station>/<date>")
def about(station, date):
    df = pandas.read_csv("")
    temperature = df.station(date)
    return render_template("about.html", station,date)

if __name__ == "__main__":
    app.run(debug=True)