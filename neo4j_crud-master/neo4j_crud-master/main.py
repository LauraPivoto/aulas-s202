from database import Database
from school_database import MatchDatabase

# cria uma instância da classe Database, passando os dados de conexão com o banco de dados Neo4j
db = Database("bolt://3.82.119.59:7687", "neo4j", "takeoffs-hood-grains")

# Criando uma instância da classe SchoolDatabase para interagir com o banco de dados
family_db = MatchDatabase(db)

print(family_db.get_engenheiros_mais_velhos_40())
print(family_db.get_filhos())
print(family_db.get_irmas())

# Fechando a conexão
db.close()