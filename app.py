from flask import Flask, render_template, request
from vegenere import encode_with_vigenere

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.hbs')

@app.route('/encrypt', methods=['POST'])
def encrypt():
    text = request.form.get('text', 'cos')
    key = request.form.get('key', 'cos2')
    want = request.form.get('select', 'encrypt')

    result = encode_with_vigenere(text, key, want)
    return render_template('index.hbs', result=result)

if __name__ == "__main__":
    app.run(debug=True)

