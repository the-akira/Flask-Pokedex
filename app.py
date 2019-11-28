from flask import Flask, render_template
import requests
import json

app = Flask(__name__)

r = requests.get('https://dadosdatascience.netlify.com/pokedex.json')
dados = r.text

pokemons = json.loads(dados)

@app.route('/')
def home():
	return render_template('home.html', pokemons=pokemons)

if __name__ == '__main__':
  app.run(debug=True)