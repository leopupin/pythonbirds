class Pessoa:
    def __init__(self, nome = None, idade = 25):
        self.idade = idade
        self.nome = nome

    def cumprimentar(self):
        return f'Olá'


if __name__ == '__main__':
    p = Pessoa('Leonardo')
    print(Pessoa.cumprimentar(p))
    print(p.cumprimentar())
    print(p.nome)
    p.nome = 'Leonardo'
    print(p.idade)