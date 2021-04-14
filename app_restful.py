from flask import Flask, request
from flask_restful import Resource,Api
import json
from habilidades import Habilidades
app = Flask(__name__)
api = Api(app)


desenvolvedores =[{
    'id':'0',
    'nome':'Alex',
    'habilidades':['Python','Flask']},
{
    'id':1,
    'nome':'Cesca',
    'habilidades':['Python','Django']}
]

class Desenvolvedor(Resource):
    def get(self,id):
        try:
            response = desenvolvedores[id]
        except IndexError:
            mensagem = 'desenvolvedor de {} não existe'.format(id)
            response = {'status':'erro','mensangem':mensagem}
        except Exception:
            mensagem = 'Erro desconhecido, procure o administgrador.'
            response = {'status': 'erro', 'mensangem': mensagem}
        return response
    def put(self,id):
        dados = json.loads(request.data)
        desenvolvedores[id] = dados
        return dados
    def delete (self):
        desenvolvedores.pop(id)
        return {'mensagem':'Registro excluido','status':'sucesso'}

class ListaDesenvolvedores(Resource):
    def get(self):
        return desenvolvedores
    def post(self):
        dados = json.loads(request.data)
        posicao = len(desenvolvedores)
        dados['id'] = posicao
        desenvolvedores.append(dados)
        return desenvolvedores[posicao]

#lista de rotas
api.add_resource(Desenvolvedor,'/dev/<int:id>/')
api.add_resource(ListaDesenvolvedores,'/dev/')
api.add_resource(Habilidades,'/habilidades/')

if __name__ == '__main__':
    app.run(debug=True)