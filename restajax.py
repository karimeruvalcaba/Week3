from flask import Flask, request, jsonify
from flask_cors import CORS

texto = "Hola"

app = Flask(__name__)
CORS(app)

@app.route("/getTest", methods=["GET", "POST"])
def get_or_post():
    if request.method == "POST":
        return "Uso un metodo POST"
    else:
        return texto

@app.route("/postTest", methods=["POST"])
def test_post():
    if request.method == "POST":
        nombre = request.json.get('nombre')  # Assuming JSON data
        email = request.json.get('email')
        global texto  # Not necessary here
        if nombre is not None:
            texto = "Hola " + nombre
            return jsonify({"message": "ok"})
        else:
            return jsonify({"message": "error", "reason": "nombre is missing"}), 400
    else:
        return jsonify({"message": "error", "reason": "Method Not Allowed"}), 405

if __name__ == "__main__":
    app.run()
