from flask import Flask, jsonify
import logging
import time

app = Flask(__name__)

# Configuración de logging para que Fluentd pueda capturarlo
logging.basicConfig(level=logging.INFO)

@app.route('/hello', methods=['GET'])
def hello():
    app.logger.info("Endpoint /hello accedido")
    return jsonify(message="Hello, CNCF!")

@app.route('/slow', methods=['GET'])
def slow():
    app.logger.info("Endpoint /slow accedido")
    time.sleep(2)  # Simula una respuesta lenta para trazarla en Jaeger
    return jsonify(message="This was a slow response")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
