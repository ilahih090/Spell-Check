# Flask Spell Checker

A simple web-based spell checker built using Flask and PySpellChecker to correct misspelled words.

## Features
- User-friendly web interface for spell checking
- Corrects individual words and full sentences
- Uses PySpellChecker for accurate spell correction
- Simple and lightweight Flask application

## Prerequisites
Ensure you have the following installed:

- Python 3.x
- Flask
- PySpellChecker

## Installation

### Clone the Repository
```sh
git clone https://github.com/ilahih090/Flask_Spell_Checker.git
cd Flask_Spell_Checker
```

### Create a Virtual Environment (Recommended)
```sh
python3 -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

### Install Dependencies
```sh
pip install -r requirements.txt
```

## Usage

### Run the Flask App
```sh
python app.py
```

### Open in Browser
Go to: [http://127.0.0.1:5000/](http://127.0.0.1:5000/)

Enter a word or sentence and get corrected spelling suggestions.

## File Structure
```
Flask_Spell_Checker/
│── static/
│   ├── styles.css  # CSS for styling
│   ├── script.js   # JavaScript (if needed)
│── templates/
│   ├── index.html  # Frontend UI
│── app.py          # Flask application
│── README.md       # Project documentation
```

## Dependencies
The project uses the following Python packages:

- **Flask**
- **pyspellchecker**
```

---

This format is clean and covers everything users need for setting up and using the Flask Spell Checker. You can easily customize or extend this as needed.

Let me know if you need any further edits! 😊
