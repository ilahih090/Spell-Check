from flask import Flask, render_template, request
from spellchecker import SpellChecker  # Import SpellChecker

app = Flask(__name__, static_folder='static')

spell = SpellChecker()  # Initialize spell checker

@app.route('/', methods=['GET', 'POST'])
def index():
    corrected_text = None
    input_text = ""

    if request.method == 'POST':
        input_text = request.form['input_text']
        words = input_text.split()  # Split input into words
        corrected_words = [spell.correction(word) if spell.correction(word) else word for word in words]  
        corrected_text = " ".join(corrected_words)  # Rejoin words

    return render_template('index.html', corrected_text=corrected_text, input_text=input_text)

if __name__ == '__main__':
    app.run(debug=True)