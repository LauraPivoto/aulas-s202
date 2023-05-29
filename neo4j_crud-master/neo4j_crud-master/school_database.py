class MatchDatabase:
    def __init__(self, database):
        self.db = database

    def get_engenheiros_mais_velhos_40(self):
        query = "MATCH (e:Engenheiro) where e.idade>=40 RETURN e"
        results = self.db.execute_query(query)
        return [result['e']['nome'] for result in results]

    def get_filhos(self):
        query = "MATCH (p:Pessoa)-[:FILHO]->() return p"
        results = self.db.execute_query(query)
        return [result['p']['nome'] for result in results]

    def get_irmas(self):
        query = "MATCH (p:Pessoa)-[:IRMA]->() return p"
        results = self.db.execute_query(query)
        return [result['p']['nome'] for result in results]