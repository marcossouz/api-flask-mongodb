from flask_restful import Resource

class Musica(Resource):
    def get(self):
        return {"listar": "musicas"}
    
    def post(self):
        return {"adicionar": "musica"}

class MusicaList(Resource):
    def get(self, id):
        return {"obter musica": "por id"}
    
    def put(self, id):
        return {"editar musica": "por id"}
    
    def delete(self, id):
        return {"remover musica": "por id"}
