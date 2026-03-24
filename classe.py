class Campus:
    def __init__(self):
        self.nome = ""
        self.cidade = ""
    def __str__(self):
        return f"Campus: {self.nome}"
class Estudante:
    def __init__(self):
        self.nome = ""
        self.dataIdade = ""
        self.cpf = ""
    def __str__(self):
        return f"Campus: {self.nome}"
    def apresentar(self):
        print(f"seu name is {self.nome} que tem idade {self.dataIdade}")
        if(self.cpf == ""):
            print(f"The studante not informed o CPF...")
        else:
            print(f"Ó o CPF da lenda",self.cpf[0:3],"...")


leo = Estudante("LeoBatata")
leo.dataIdade = "14/??/2009"
leo.cpf = "404.057.777-67" #cpf mais aleatério que ja dive
boeno = Estudante()
boeno.nome = "Sabriel Bobassouro"
boeno.dataIdade = "??/04/2009"
boeno.apresentar()
leo.apresentar()