from flask import Flask, Blueprint
from flask_restful import Api

from api.resources.livro import Livro, LivroList
from api.resources.musica import Musica, MusicaList

app = Flask(__name__)
api_bp = Blueprint('api', __name__)
api = Api(api_bp)

api.add_resource(Livro, '/livro')
api.add_resource(LivroList, '/livro/<string:id>')
api.add_resource(Musica, '/musica')
api.add_resource(MusicaList,'/musica/<string:id>')

app.register_blueprint(api_bp)

if __name__ == '__main__':
    app.run(debug=True)