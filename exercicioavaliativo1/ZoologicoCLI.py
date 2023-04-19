import ZoologicoDAO
from main import *
from ZoologicoDAO import *

class SimpleCLI:
    def __init__(self):
        self.commands = {}

    def add_command(self, name, function):
        self.commands[name] = function

class AnimalCLI(AnimalModel):
    def __init__(self):
        super().__init__(self)

    def run(self):
        while True:
            command = input("Escolha o que deseja fazer: ")

            if command == "Criar":
                AnimalCLI.create(self)
            elif command == "Ler":
                AnimalCLI.read(self)
            elif command == "Apagar":
                AnimalCLI.delete(self)
            elif command == "Dar update":
                AnimalCLI.update(self)

            if command == "Sair":
                print("Até mais!")
                break

    def create(self):
        nome = input("Digite o nome do cuidador que deseja criar: ")
        documento = input("Digite o documento do mesmo: ")
        cuidador = Cuidador(nome, documento)

        haCuidador = []
        habitatsCuidador = int(input("Qual o número de Habitats desse cuidador? Ele precisa de pelo menos 1"))
        for i in range(habitatsCuidador):
            nome = input("Digite o nome desse habitat")
            tipo = input("Digite o tipo do ambiente:")
            habitat = Habitat(nome, tipo, cuidador)
            haCuidador.append(vars(habitat))

        nomeAnimal = input("Digite o nome do animal")
        especieAnimal = input("Digite a especie do animal")
        idadeAnimal = int(input("Digite a idade do animal"))

        ZoologicoDAO.AnimalModel.create_Animal(self, nomeAnimal, especieAnimal, idadeAnimal, haCuidador)

    def read(self):
        id = str(input("Entre com o id: "))
        ZoologicoDAO.AnimalModel.read_animal_by_id(self, id)

    def update(self):
        nomeAnimal = input("Digite o nome do animal")
        especieAnimal = input("Digite a especie do animal")
        idadeAnimal = int(input("Digite a idade do animal"))

        nome = input("Digite o nome do cuidador que deseja criar: ")
        documento = input("Digite o documento do mesmo: ")
        cuidador = Cuidador(nome, documento)

        haCuidador = []
        habitatsCuidador = int(input("Qual o número de Habitats desse cuidador? Ele precisa de pelo menos 1"))
        for i in range(habitatsCuidador):
            nome = input("Digite o nome desse habitat")
            tipo = input("Digite o tipo do ambiente:")
            habitat = Habitat(nome, tipo, cuidador)
            haCuidador.append(vars(habitat))

        id = str(input("Entre com o id: "))
        ZoologicoDAO.AnimalModel.update_animal(self, id, nomeAnimal, especieAnimal, idadeAnimal, haCuidador)

    def delete(self):
        id = str(input("Entre com o id: "))
        ZoologicoDAO.AnimalModel.read_animal_by_id(self, id)
