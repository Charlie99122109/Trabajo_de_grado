from flask import Flask, jsonify, request

app = Flask(__name__)

from datos import becas

@app.route('/ping')
def ping():
    return jsonify({"mensaje": "Helou beibe"})

@app.route('/datos')
def imprimirDatos():
    return jsonify(becas)

@app.route('/datos/<string:nombre_beca>')
def getDato(nombre_beca):
    becaEncontrada = [beca for beca in becas if beca['nombre'] == nombre_beca]
    return jsonify({"BECA": becaEncontrada[0]})

@app.route('/datos', methods=['POST'])
def añadirBeca():
    print(request.json)
    return 'Recibido'

if __name__ == '__main__':
    app.run(debug = True, port = 5000)