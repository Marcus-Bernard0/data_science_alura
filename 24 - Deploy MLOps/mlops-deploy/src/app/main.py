
from flask import Flask, request, jsonify
from flask_basicauth import BasicAuth
from textblob import TextBlob
from sklearn.linear_model import LinearRegression
import pickle
import os

# importando o modelo gravado
colunas = ['tamanho', 'ano', 'garagem']
modelo = pickle.load(open('models\modelo.sav', 'rb'))

app = Flask(__name__)
app.config['BASIC_AUTH_USERNAME'] = 'marcus'
app.config['BASIC_AUTH_PASSWORD'] = '123'

basic_auth = BasicAuth(app)

# definindo uma rota


@app.route('/')
def home():
    return "<h1>Minha primeira API.<h1>"

# end point


@app.route('/sentimento/<frase>')
@basic_auth.required
def sentimento(frase):

    tb = TextBlob(frase)
    tb_en = tb.translate(from_lang='pt_br', to='en')
    polaridade = tb_en.sentiment.polarity
    return "O nivel de polaridade é de -1 a 1. (negativo: triste, positivo: Feliz. Sua Polaridade é: {}" .format(polaridade)


@app.route('/cotacao/', methods=['POST'])
@basic_auth.required
def cotacao():
    dados = request.get_json()
    dados_input = [dados[col] for col in colunas]
    preco = modelo.predict([dados_input])
    return jsonify(preco=preco[0])


app.run(debug=True, host = '0.0.0.0')

