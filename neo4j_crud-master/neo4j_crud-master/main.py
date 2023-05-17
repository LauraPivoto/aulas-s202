from database import Database
from school_database import MatchDatabase

# cria uma instância da classe Database, passando os dados de conexão com o banco de dados Neo4j
db = Database("bolt://44.202.231.76:7687", "neo4j", "bunches-spindle-boil")
db.drop_all()

# Criando uma instância da classe SchoolDatabase para interagir com o banco de dados
school_db = MatchDatabase(db)


# Fechando a conexão
db.close()