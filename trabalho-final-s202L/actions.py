class MatchDatabase:
    def __init__(self, database):
        self.db = database

    def create(self, name, ano_nasc, cpf):
        query = "CREATE (:Professor {name: $name, anonasc: $ano_nasc, cpf: $cpf})"
        parameters = {"name": name, 'ano_nasc': ano_nasc, 'cpf': cpf}
        self.db.execute_query(query, parameters)

    def read(self, name):
        query = "MATCH (p:Professor) where p.name = $name RETURN p.name "
        parameters = {"name": name}
        self.db.execute_query(query, parameters)

    def delete(self, name):
        query = "MATCH (p:Professor {name: $name}) DETACH DELETE p"
        parameters = {"name": name}
        self.db.execute_query(query, parameters)

    def update_professor(self, name, new_cpf):
        query = "MATCH (p:Professor {name: $name}) SET p.cpf = $new_cpf"
        parameters = {"name": name, "new_cpf": new_cpf}
        self.db.execute_query(query, parameters)