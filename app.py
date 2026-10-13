from flask import Flask, jsonify, render_template
from pathlib import Path
import json

app = Flask(__name__)
QUESTIONS = json.loads((Path(__file__).parent / 'questions_modulo2.json').read_text(encoding='utf-8'))


@app.get('/')
def home():
    return render_template('index.html')


@app.get('/api/modulo2')
def questions():
    return jsonify(QUESTIONS)


if __name__ == '__main__':
    app.run(debug=True)
