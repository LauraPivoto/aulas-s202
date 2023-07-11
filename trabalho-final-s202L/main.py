from database import Database
from actions import MatchDatabase

# cria uma instância da classe Database, passando os dados de conexão com o banco de dados Neo4j
db = Database("bolt://3.82.119.59:7687", "neo4j", "takeoffs-hood-grains")

# Criando uma instância da classe SchoolDatabase para interagir com o banco de dados
family_db = MatchDatabase(db)

def exibir_menu():
    print("Bem-vindo(a) ao programa!")
    print("Aqui estão as ações disponíveis:")
    print("1. Ação 1")
    print("2. Ação 2")
    print("3. Ação 3")
    print("4. Sair")

def executar_acao(acao):
    if acao == 1:
        print("Executando a Ação 1...")
        # Lógica da Ação 1
    elif acao == 2:
        print("Executando a Ação 2...")
        # Lógica da Ação 2
    elif acao == 3:
        print("Executando a Ação 3...")
        # Lógica da Ação 3
    elif acao == 4:
        print("Encerrando o programa...")
        return False
    else:
        print("Opção inválida. Por favor, escolha uma ação válida.")

    return True

# Função principal
def main():
    exibir_menu()

    executar = True
    while executar:
        acao = int(input("Escolha uma ação (1-4): "))
        executar = executar_acao(acao)

# Chamada da função principal
main()

#print(family_db.get_engenheiros_mais_velhos_40())
#print(family_db.get_filhos())
#print(family_db.get_irmas())

# Fechando a conexão
db.close()