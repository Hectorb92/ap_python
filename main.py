
# POR TERMINAL
# python -m pip install flask 
from flask import Flask, jsonify

app = Flask (__name__)


# Ejemplo 1 
'''
from productos import productos
@app.route('/ping')
def ping():
    return 'pong' 
    
'''
# Ejemplo 2 
from productos import productos
@app.route('/ping')
def ping():
    return 







if __name__ == "__main__":
    app.run(debug=True, port=4000)