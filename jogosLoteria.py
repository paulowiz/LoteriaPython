import random


class jogosLoteria:

    def __init__(self, qtd, resultado, totalJogos, jogos):  # classe solicitada
        self.qtd = qtd
        self.resultado = resultado
        self.totalJogos = totalJogos
        self.jogos = jogos

    def get(self):  # Metodo para retornoar os valores da classe
        retorno = "Quantidade:%s  Resultado: %s  Total de jogos: %s Jogos: %s" % (
            self.qtd, self.resultado, self.totalJogos, self.jogos)
        return retorno

    def set(self, qtd, resultado, totalJogos, jogos):  # metodo para modificar os valores da classe

        self.qtd = qtd
        self.resultado = resultado
        self.totalJogos = totalJogos
        self.jogos = jogos

    # Recebe a quantidade de dezenas e o resultado
    def recebeInformacoes(self, qtd, totalJogos):
        self.resultado = resultado
        self.totalJogos = totalJogos

    # retorna dezenas aleatóras e a quantidada informada pela classe
    def retornaDezenas(self):
        array = (random.sample(range(1, 60), self.qtd))
        array.sort()
        return array

    def intersecao(self, conjunto):  # Verifica quais numeros em cada jogo contem no resultado
        intersecao = []
        for elemento in self.resultado:
            if (elemento in conjunto):
                intersecao.append(elemento)
        return intersecao


pass
