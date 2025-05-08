from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/send', methods=['POST'])
def send_message():
    data = request.json
    numero = data.get("numero")
    mensagem = data.get("mensagem")
    print(f"📨 Mensagem recebida: {numero} - {mensagem}")
    return jsonify({"status": "mensagem recebida com sucesso"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
