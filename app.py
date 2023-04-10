from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Fabrício Nunes de Araújo | RA:22010 // Guilherme Augusto Alves Pereira da Silva | Ra: 220097'