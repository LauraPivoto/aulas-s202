#A classe deve conter métodos para criar, atualizar, recuperar e excluir jogadores e partidas,
# bem como para registrar resultados de partidas entre jogadores.

class SchoolDatabase:
    def __init__(self, database):
        self.db = database

    def create_jogador(self, name):
        query = "CREATE (:Jogador {name: $name})"
        parameters = {"name": name}
        self.db.execute_query(query, parameters)

    def create_partida(self, name, ganhador):
        query = "CREATE (:Partida {name: $name, ganhador: 'nenhum'})"
        parameters = {"name": name,"ganhador": ganhador},
        self.db.execute_query(query, parameters)

    def update_jogador(self, old_name, new_name):
        query = "MATCH (p:Jogador {name: $old_name}) SET p.name = $new_name"
        parameters = {"old_name": old_name, "new_name": new_name}
        self.db.execute_query(query, parameters)

    def update_partida(self, old_winner, new_winner):
        query = "MATCH (p:partida {: $old_winner}) SET p.ganhador = $new_winner"
        parameters = {"old_name": old_winner, "new_name": new_winner}
        self.db.execute_query(query, parameters)

    def get_jogador(self):
        query = "MATCH (j:Jogador) RETURN j.name AS name"
        results = self.db.execute_query(query)
        return [result["name"] for result in results]

    def get_partida_info(self):
        query = "MATCH (p:Partida) RETURN p.name AS partida_name, p.ganhador as partida_ganhador"
        results = self.db.execute_query(query)
        return [(result["name"], result["partida_ganhador"]) for result in results]

    def get_partida(self):
        query = "MATCH (p:Partida)<-[:JOGA]-(j:Jogador) RETURN j.name AS name, p.name AS partida_name"
        results = self.db.execute_query(query)
        return [(result["name"], result["partida_name"]) for result in results]

    def delete_jogador(self, name):
        query = "MATCH (j:Jogador {name: $name}) DETACH DELETE p"
        parameters = {"name": name}
        self.db.execute_query(query, parameters)

    def delete_partida(self, name):
        query = "MATCH (p:Partida {name: $name}) DETACH DELETE p"
        parameters = {"name": name}
        self.db.execute_query(query, parameters)


