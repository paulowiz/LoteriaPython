from jogosLoteria import jogosLoteria
import random
from flask import Flask, request
from flask_table import Table, Col

qtd = input('Informe a quantidade de dezenas:')

while (int(qtd) < 6) or (int(qtd) > 10):
    print('Quantidade de dezenas inválida! Deve ser entre [6,7,8,9,10]')
    qtd = input('Informe a quantidade de dezenas:')

totalJogos = input('Informe a quantidade de jogos: ')

totalJogos = int(totalJogos)
qtd = int(qtd)

lot = jogosLoteria(qtd, 0, totalJogos, 0)  # qtd, resultado, totalJogos, jogos


def geraJogos():  # gera todos os jogos de acordo com a quantidade solicitada na classe
    jogos = []
    i = 0
    while i < lot.totalJogos:
        jogos.append(lot.retornaDezenas())
        i += 1
    return jogos


def geraResultado():  # gera uma dezena de 6 digitos aleatória e sem repetição que utilizará no resultado
    array = (random.sample(range(1, 60), 6))
    array.sort()
    return array


# Metodo que verifica a quantidade acertada e retorna o html
def confereJogos(resultado, jogos):
    app = Flask(__name__)

    s = '<table align ="center" size="80"><caption>Loteria America</caption><tr><td>Resultado</td><td>%s</td></tr></table>' % (
        str(resultado))
    s = s + '<table align ="center" border="1px"> <thead><tr><td>Jogos</td><td>Acertos</td></tr> </thead>'
    s = s + "<tr>"
    for x in jogos:
        acc = lot.intersecao(x)
        s = s + "<td >" + str(x) + "</td>"+"<td>" + str(len(acc)) + "</td>"
        s = s + "</tr>"
    s = s + "</table>"

    @app.route("/")
    def hello():
        return "<html><body>" + s + "</body></html>"

    if __name__ == "__main__":
        app.run()


lot.jogos = geraJogos()  # atribui no objeto os jogos gerados
lot.resultado = geraResultado()  # atribui no objeto o resultado gerado aleatório
print('Verifique o resultado da loteria em http://127.0.0.1:5000/')
# Calcula e exibe o resultado no endereço http://127.0.0.1:5000/
confereJogos(lot.resultado, lot.jogos)
