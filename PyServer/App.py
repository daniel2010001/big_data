# from flask import Flask, request, jsonify
# import subprocess

# app = Flask(__name__)

# @app.route('/run-script', methods=['GET'])
# def run_script():
#     try:
#         # Ejecutar el script de Python
#         result = subprocess.run(['python', 'script.py'], capture_output=True, text=True)
#         return jsonify(output=result.stdout)
#     except Exception as e:
#         return jsonify(error=str(e)), 500

# if __name__ == '__main__':
#     app.run(debug=True)

# VERSION v2

# from flask import Flask, request, jsonify
# from flask_cors import CORS
# import subprocess

# app = Flask(__name__)
# CORS(app)  # Habilitar CORS para todas las rutas

# @app.route('/run-script', methods=['GET'])
# def run_script():
#     try:
#         # Ejecutar el script de Python
#         result = subprocess.run(['python', 'script.py'], capture_output=True, text=True)
#         return jsonify(output=result.stdout)
#     except Exception as e:
#         return jsonify(error=str(e)), 500

# if __name__ == '__main__':
#     app.run(debug=True)

# VERSION v3

from flask import Flask, request, jsonify
from flask_cors import CORS
import subprocess

app = Flask(__name__)
CORS(app)  # Habilitar CORS para todas las rutas

@app.route('/scraping', methods=['POST'])
def run_script():
    try:
        # Obtener los parámetros del cuerpo de la solicitud
        parametro1 = request.json.get('parametro1')
        parametro2 = request.json.get('parametro2')

        # Verificar que ambos parámetros estén presentes
        if not parametro1 or not parametro2:
            return jsonify(error='Faltan parámetros en la solicitud'), 400

        # Ejecutar el script de Python con los parámetros
        result = subprocess.run(['python', 'scapyPaginas.py', parametro1, parametro2], capture_output=True, text=True)
        
        # Devolver la salida del script como respuesta
        return jsonify(output=result.stdout)
    except Exception as e:
        return jsonify(error=str(e)), 500

if __name__ == '__main__':
    app.run(debug=True)
