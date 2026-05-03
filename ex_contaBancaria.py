class Aluno:
    def __init__(self, nome, idade, curso, nota):
        self.nome = nome
        self.idade = idade
        self.curso = curso
        self.ra = ""
        self.nota = nota

    def apresentar(self):
        print(f"Olá, meu nome é {self.nome}, tenho {self.idade} anos e sou do curso de {self.curso}")
        if(self.ra == ""):
            print("Esse aluno não possuie RA")
            while(self.ra == ""):
                self.ra = input("Informe o RA: ")
        else:
            print(f" O RA é: {self.ra}")
    def calcular_media(self):
        soma = 0.0
        for i in range(0, len(self.nota)):
            soma += self.nota(i)
        media = soma/len(self.nota)
        return media
class Turma:
    def __init__(self, nome, ano):
        self.nome = nome
        self.ano = ano
        self.estudantes = []




nome = input("Digite o seu nome: ")
idade = int(input("Digite sua idade: "))
curso = input("Digite o seu curso: ")
nota = int(input("Digite sua nota: "))

alun1 = Aluno(nome, idade, curso, nota)
alun1.apresentar()