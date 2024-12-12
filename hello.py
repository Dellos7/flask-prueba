from flask import Flask, render_template, request, url_for
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

@app.route('/temperatura')
def temp():
    return render_template('temperatura.html')

@app.post('/convertir')
def convertir():
    celsius = int(request.form.get('celsius'))
    fahrenheit = celsius*9 / 5 + 32
    kelvin = celsius + 273.15
    #return f'Celsius: {celsius}<br>Farenheit: {fahrenheit}<br>Kelvin: {kelvin}'
    return render_template('resultado.html', celsius=celsius, fahrenheit=fahrenheit, kelvin=kelvin)

