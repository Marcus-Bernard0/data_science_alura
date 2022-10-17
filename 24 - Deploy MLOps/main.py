from flask import Flask
from textblob import TextBlob
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# modelo de ML
import pandas as pd
url = 'https://raw.githubusercontent.com/alura-cursos/1576-mlops-machine-learning/aula-5/casas.csv'
df = pd.read_csv(url)
colunas = ['tamanho', 'preco']
df = df[colunas]
X = df.drop('preco', axis=1)
y = df['preco']
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42)
modelo = LinearRegression()
modelo.fit(X_train, y_train)
app = Flask(__name__)


# definindo uma rota
@app.route('/')
def home():
    return "Minha primeira API."

# end point


@app.route('/sentimento/<frase>')
def sentimento(frase):

    tb = TextBlob(frase)
    tb_en = tb.translate(from_lang='pt_br', to='en')
    polaridade = tb_en.sentiment.polarity
    return "O nivel de polaridade é de -1 a 1. (negativo: triste, positivo: Feliz. Sua Polaridade é: {}" .format(polaridade)


@app.route('/cotacao/<int:tamanho>')
def cotacao(tamanho):
    preco = modelo.predict([[tamanho]])
    return str(preco)


app.run(debug=True)
