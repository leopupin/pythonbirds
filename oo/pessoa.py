class Pessoa:
    def __init__(self, *filhos, nome = None, idade = 25):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá'


if __name__ == '__main__':
    leonardo = Pessoa(nome='Leonardo')
    renzo = Pessoa(leonardo, nome='Renzo')
    print(leonardo.cumprimentar())
    print(leonardo.nome)
    print(leonardo.idade)
    for filho in renzo.filhos:
        print(filho.nome)
    leonardo.sobrenome = "Pupin"
    del renzo.filhos
    print(leonardo.__dict__)
    print(renzo.__dict__)
