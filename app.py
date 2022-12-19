from flask import Flask, render_template, request

app = Flask(__name__)

def encode_with_vigenere(text, key, want):
    text = text.upper()
    key = key.upper()
    result = ''
    for i in range(len(text)):
        if text[i] == ' ':
            result += ' '
        else:
            if want == 'encrypt':
                result += chr((ord(text[i]) + ord(key[i % len(key)])) % 26 + ord('A'))
            else:
                result += chr((ord(text[i]) - ord(key[i % len(key)])) % 26 + ord('A'))
    return result




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

