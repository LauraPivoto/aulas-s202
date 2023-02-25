# Relatório 1

class Animal:
    def __init__(self, nome, idade, especie, cor, som):
        self.nome = nome
        self.idade = idade
        self.especie = especie
        self.cor = cor
        self.som = som

    def mudar_cor(self, nova_cor):
        self.cor = nova_cor
        return f"{self.nome} mudou para a cor: {nova_cor}"

    def emitir_som(self):
        return f"Som do animal: {self.som}"


class Elefante(Animal):
    def __int__(self, nome, idade, especie, cor, som, tamanho):
        super().__init__(nome, idade, especie, cor, som)
        self.tamanho = tamanho

    def trombar(self):
        return f"Som do elefante: {self.som}"

    def mudar_tamanho(self, novo_tamanho):
        self.tamanho = novo_tamanho


print("Agora vamos criar o seu elefante")

nome_elefante = input("Digite o nome do seu elefante: ")
idade_elefante = input("Digite a idade do seu elefante: ")
especie_elefante = input("Digite a especie do seu elefante: ")
cor_elefante = input("Digite a cor do seu elefante: ")
tamanho_elefante = input("Digite o tamanho do seu elefante: ")

if especie_elefante == "Africano":
    if idade_elefante < 10:
        tamanho_elefante = "pequeno"
        som_elefante = "Paaah"
    else:
        tamanho_elefante = "grande"
        som_elefante = "PAAAAAHHH"
else:
    som_elefante = "som de elefante"

elefante = Elefante(nome_elefante, idade_elefante, especie_elefante, cor_elefante, som_elefante, tamanho_elefante)

print("Características do Elefante: " + elefante.nome + ", " + elefante.idade + ", " + elefante.especie
      + ", " + elefante.cor + ", " + elefante.tamanho + ", " + elefante.som)


