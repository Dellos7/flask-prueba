from flask import Flask
from markupsafe import escape

app = Flask(__name__)


@app.route('/')
def hello():
    return '<p><b>Hello</b>, <u>World!</u></p>'


@app.route('/hola')
def hola():
    return 'Hola!'

@app.route('/hola/<usuario>')
def hola_usuario(usuario):
    #return 'Hola ' + usuario + '!'
    return f'Hola {escape(usuario)}!'

# El nombre de la variable que indicamos en la ruta debe coincidir con el nombre de la variable en la función
# Tipos permitidos: int, string, float, path, uuid
# El tipo "path" acepta barras
@app.route('/numero/<int:x>')
def x2(x):
    mult = x*2
    return f'El doble de {x} es {mult}'
