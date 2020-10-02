from flask_restful import Resource

class Livro(Resource):
    def get(self):
        return {"listar": "livros"}
    
    def post(self):
        return {"adicionar": "livro"}

class LivroList(Resource):
    def get(self, id):
        return {"obter livro": "por id"}
    
    def put(self, id):
        return {"editar livro": "por id"}
    
    def delete(self, id):
        return {"remover livro": "por id"}
