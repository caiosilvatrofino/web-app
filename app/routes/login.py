from flask import Flask, Blueprint, request, jsonify

login = Blueprint('login',__name__)


@login.route('/login', methods=['GET','POST'])
def login_autentication():
    credenciais = request.json
    username = credenciais.get('nome')
    password = credenciais.get('senha')
    if username != 'lucas':
        return jsonify(msg='usuario não autorizado!')
    
    if password != 'dadsdadasdsadaeqweq':
        return jsonify(msg='senha invalida, tente novamente!')
    return jsonify(msg='Logou com sucesso!')
    

def init(app: Flask):
    app.register_blueprint(login)
