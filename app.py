from flask import Flask, request, jsonify
from twilio.rest import Client
import logging
import os
import sqlite3

app = Flask(__name__)

# Configurações do Twilio
TWILIO_SID = os.getenv('TWILIO_SID')
TWILIO_AUTH_TOKEN = os.getenv('TWILIO_AUTH_TOKEN')
TWILIO_PHONE_NUMBER = os.getenv('TWILIO_PHONE_NUMBER')
client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

logging.basicConfig(level=logging.INFO)

def init_db():
    """Inicializa o banco de dados e cria a tabela de mensagens se não existir."""
    with sqlite3.connect('database.db') as conn:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS messages (
                id INTEGER PRIMARY KEY,
                from_number TEXT,
                message TEXT,
                response TEXT
            )
        ''')
        conn.commit()

def log_message(from_number, message, response):
    """Registra a mensagem e a resposta no banco de dados."""
    with sqlite3.connect('database.db') as conn:
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO messages (from_number, message, response)
            VALUES (?, ?, ?)
        ''', (from_number, message, response))
        conn.commit()

@app.route('/whatsapp', methods=['POST'])
def whatsapp_reply():
    """Recebe mensagens do WhatsApp e responde com base no conteúdo da mensagem."""
    incoming_msg = request.form.get('Body', '').strip().lower()
    from_number = request.form.get('From')

    logging.info(f"Received message: {incoming_msg} from {from_number}")

    # Determina a resposta com base na mensagem recebida
    if 'pedido' in incoming_msg:
        response = ("Ótimo! Como posso ajudá-lo com seu pedido? Por favor, informe o item ou serviço desejado.")
    elif 'informações sobre o menu' in incoming_msg:
        response = ("Claro! Podemos fornecer informações sobre nossos produtos e serviços. O que você gostaria de saber?")
    elif 'status do pedido' in incoming_msg:
        response = ("Para verificar o status do seu pedido, por favor, forneça o número do pedido ou o nome associado ao pedido.")
    elif 'promoções' in incoming_msg:
        response = ("Atualmente, temos as seguintes promoções: [Descreva promoções atuais aqui].")
    elif 'outras dúvidas' in incoming_msg:
        response = ("Por favor, descreva sua dúvida ou questão, e faremos o nosso melhor para ajudar.")
    else:
        response = ("Olá! Sou o assistente virtual. Como posso ajudar você hoje?")

    # Envia a resposta de volta ao usuário
    client.messages.create(
        body=response,
        from_=TWILIO_PHONE_NUMBER,
        to=from_number
    )

    logging.info(f"Sent response: {response} to {from_number}")

    # Registra a mensagem e a resposta
    log_message(from_number, incoming_msg, response)

    return jsonify({"status": "success"})

if __name__ == '__main__':
    init_db()
    app.run(port=5000)
