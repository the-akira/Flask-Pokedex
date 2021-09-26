from flask import Flask, render_template
import requests
import json

app = Flask(__name__)

r = requests.get('https://gist.githubusercontent.com/the-akira/4f2244540d61f8a9d3ec73b280af5f9b/raw/7d55ea6600b25292d4e0b8b76743204403747e38/pokedex.json')
dados = r.text

pokemons = json.loads(dados)

@app.route('/')
def home():
    return render_template('home.html', pokemons=pokemons)

if __name__ == '__main__':
    app.run(debug=True)