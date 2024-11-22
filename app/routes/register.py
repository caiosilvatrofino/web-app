from flask import Blueprint, Flask, request, jsonify
from app.database import add_new_user,User


register = Blueprint('register',__name__)


@register.route('/register', methods=['GET','POST'])
def register_new_user():
    register = request.json
    newuser = add_new_user(register.get('username'), register.get('password'))
    return jsonify(msg= "Usuario registrado!")


def init(app:Flask):
    app.register_blueprint(register)