from flask import Flask, render_template
from jinja2 import Template

app = Flask(__name__)

@app.route("/")
def task():
    return render_template("task.html")
    
@app.route("/api/v1/<word>")
def translate_word(word):
    definition= word.upper()
    result_dictionary = {'word': word, 'definition': definition}
    return result_dictionary




if __name__ == "__main__":
    app.run(debug=True, port=5001)