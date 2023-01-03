from flask import Flask, render_template, request
from vigenere import vigenere

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        text = request.form['text']
        key  = request.form['key']
        want = request.form['select']

        return render_template('index.hbs', result=vigenere(text, key, want))
    return render_template('index.hbs')


if __name__ == "__main__":
    app.run(debug=True)

