from flask import Flask, request
import pickle
from flask_cors import CORS

application = Flask(__name__)
CORS(application)

@application.route('/flask', methods=['GET'])
def flask():
    return '<p><a href="https://flask.palletsprojects.com/en/2.2.x/">https://flask.palletsprojects.com/en/2.2.x/</a></p>'

@application.get('/api/get')
def get_method():
    word = request.args.get('word', '<no word>')
    return {
        'hello': 'hello, ' + word
    }

@application.route('/')
def main():
    return '<p>Hello, World!</p>'

@application.get('/polo')
def polo():
    with open('cochesnet.pck', 'rb') as file:
        dv, model = pickle.load(file)

    coche = {
        'marca': 'vw',
        'modelo': 'polo',
        'cv': 110
    }

    coche_bien_codificado = dv.transform(coche)
    precio = model.predict(coche_bien_codificado)
    return {
        'precio': precio[0]
    }

@application.get('/car')
def car():
    with open('cochesnet.pck', 'rb') as file:
     dv, neural_model = pickle.load(file)

    # obtenemos el coche de la request

    # marca = request.args.get('marca', '')
    # modelo = request.args.get('modelo', '')
    # cv_str = request.args.get('cv', '0')
    # cv = int(cv_str)

    color = request.args.get('color', '')
    fuelType = request.args.get('fuelType', '')
    km = int(request.args.get('km', ''))
    make = request.args.get('make', '')
    model = request.args.get('model', '')
    province = request.args.get('province', '')
    transmissionType = request.args.get('transmissionType', '')
    year = int(request.args.get('year', ''))
    seller_type = request.args.get('seller_type', '')
    bodyType = request.args.get('bodyType', '')
    cubicCapacity = request.args.get('cubicCapacity', '')
    doors = request.args.get('doors', '')
    hp = request.args.get('hp', '')

    coche = {
        'color': color,
        'fuelType': fuelType,
        'km': km,
        'make': make,
        'model': model,
        'province': province,
        'transmissionType': transmissionType,
        'year': year,
        'seller_type': seller_type,
        'bodyType': bodyType,
        'cubicCapacity': cubicCapacity,
        'doors': doors,
        'hp': hp,
    }

    coche= {
        'marca':  marca,
        'modello': modelo,
        'cv': cv
    }
    coche_bien_codificado= dv.transform(coche)
    
    try:
        precio = neural_model.predict(coche_bien_codificado)
    except:
         precio = 0
         
    return {
         'precio': precio[0]
    }


application.run()