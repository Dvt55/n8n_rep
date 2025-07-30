from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

URL_WEBHOOK = "https://dmelon8n.app.n8n.cloud/webhook-test/atvd2"

@app.route('/api/reenviar', methods=['POST'])

def reenviar_para_webhook():
    try:
        resposta = request.data.decode('utf-8')

        resposta = requests.post(URL_WEBHOOK, data=resposta, headers={"Content-Type": "text/plain"})

        return jsonify({
                "resposta" : resposta.json()
        }), resposta.status_code
    
    except Exception as e:
        return jsonify({"erro": str(e)}), 500
    
if __name__ == '__main__':
    app.run(debug=True)




    