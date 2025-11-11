from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/meaning', methods=['GET'])
def get_meaning():
    word = request.args.get('word')
    if not word:
        return jsonify({'error': 'Please provide a word'}), 400

    url = f'https://api.dictionaryapi.dev/api/v2/entries/en/{word}'
    response = requests.get(url)

    if response.status_code != 200:
        return jsonify({'error': 'Word not found'}), 404

    data = response.json()[0]
    meaning = data['meanings'][0]['definitions'][0]['definition']
    example = data['meanings'][0]['definitions'][0].get('example', 'No example available')
    phonetic = data.get('phonetic', 'N/A')

    result = {
        'word': word,
        'phonetic': phonetic,
        'meaning': meaning,
        'example': example
    }
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
