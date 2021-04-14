from flask import Flask, jsonify, request
import json
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

app = Flask(__name__)
desenvolvedores =[{
    'id':'0',
    'nome':'Alex',
    'habilidades':['Python','Flask']},
{
    'id':1,
    'nome':'Cesca',
    'habilidades':['Python','Django']}
]
#devolve o desenvolvedor por ai, altera e delata.
@app.route('/dev/<int:id>/',methods=['GET','PUT','DELETE'])
def desenvolvedor(id):
    if request.method =='GET':
        try:
            response = desenvolvedores[id]
        except IndexError:
            mensagem = 'desenvolvedor de {} não existe'.format(id)
            response = {'status':'erro','mensangem':mensagem}
        return jsonify(response)
    elif request.method == 'PUT':
        dados = json.loads(request.data)
        desenvolvedores[id] = dados
        return jsonify(dados)
    elif request.method == 'DELETE':
        desenvolvedores.pop(id)
        return jsonify({'mensagem':'Registro excluido','status':'sucesso'})
#lista os desenvolvedores e permite registrar um novo desenvolvedor.
@app.route('/dev/',methods=['POST','GET'])
def lista_desenvolvedores():
    if request.method == 'POST':
        dados = json.loads(request.data)
        posicao = len(desenvolvedores)
        dados['id'] = posicao
        desenvolvedores.append(dados)
        return jsonify(desenvolvedores[posicao])
    elif request.method == 'GET':
        return jsonify(desenvolvedores)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app.run(debug=True)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
