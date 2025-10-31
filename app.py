from flask import Flask, send_from_directory
from flask_cors import CORS

app = Flask(__name__, static_folder=".")
CORS(app)

@app.route("/api")
def swagger_ui():
    return send_from_directory(".", "index.html")

@app.route("/openapi.yaml")
def openapi_file():
    return send_from_directory(".", "openapi.yaml")

@app.route("/")
def home():
    return {
        "message": "Digitální evidence doporučení SPU API - přejděte na /api pro Swagger dokumentaci"
    }

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
