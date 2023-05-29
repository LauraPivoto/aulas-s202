from database import Database
from school_database import SchoolDatabase

# cria uma instância da classe Database, passando os dados de conexão com o banco de dados Neo4j
db = Database("bolt://3.218.208.95:7687", "neo4j", "partners-stall-assembly")

# Criando uma instância da classe SchoolDatabase para interagir com o banco de dados
school_db = SchoolDatabase(db)

# Criando alguns professores
#school_db.create("Chris Lima", 1956, '189.052.396-66')
print(school_db.read('Chris Lima'))
school_db.update_professor('Chris Lima', '162.052.777-77')

# Fechando a conexão
db.close()