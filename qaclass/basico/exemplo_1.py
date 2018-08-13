'''Caracteristicas gerais'''


class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    #Representa a classe, sempre retorna uma string
    def __repr__(self):
        return f'Pessoa(nome:{self.nome}, idade={self.idade}'
