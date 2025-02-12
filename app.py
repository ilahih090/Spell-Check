from flask import Flask, render_template, request
from spellchecker import SpellChecker  

app = Flask(__name__, static_folder='static')

spell = SpellChecker()  

@app.route('/', methods=['GET', 'POST'])
def index():
    corrected_text = None
    input_text = ""
    suggestions = {}

    if request.method == 'POST':
        input_text = request.form['input_text']
        words = input_text.split()  

        corrected_words = []
        for word in words:
            correction = spell.correction(word)
            corrected_words.append(correction if correction else word)

            # Get spelling suggestions for misspelled words
            if word not in spell:
                suggestions[word] = spell.candidates(word)

        corrected_text = " ".join(corrected_words)  

    return render_template('index.html', corrected_text=corrected_text, input_text=input_text, suggestions=suggestions)

if __name__ == '__main__':
    app.run()
