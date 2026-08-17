from flask import Flask, request

app = Flask(__name__)

@app.route("/uplink", methods=["POST"])
def uplink():
    print("Message reçu :", request.json)
    return {"status": "ok"}

app.run(host="0.0.0.0", port=10000)
