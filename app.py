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
    with sqlite3.connect('database.db') as conn:
        cursor = conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS messages
                          (id INTEGER PRIMARY KEY, from_number TEXT, message TEXT, response TEXT)''')
        conn.commit()

def log_message(from_number, message, response):
    """Registra a mensagem e a resposta no banco de dados"""
    with sqlite3.connect('database.db') as conn:
        cursor = conn.cursor()
        cursor.execute('INSERT INTO messages (from_number, message, response) VALUES (?, ?, ?)',
                       (from_number, message, response))
        conn.commit()

@app.route('/whatsapp', methods=['POST'])
def whatsapp_reply():
    incoming_msg = request.form.get('Body', '').strip().lower()
    from_number = request.form.get('From')

    logging.info(f"Received message: {incoming_msg} from {from_number}")

    response = ""

    if 'pedido' in incoming_msg:
        response = ("Ótimo! Para começar, qual tipo de pizza você gostaria de pedir? "
                    "Temos opções como Margherita, Pepperoni, Quatro Queijos, entre outras.")
    elif 'informações sobre o menu' in incoming_msg:
        response = ("Claro! Nosso menu inclui uma variedade de pizzas, massas, saladas e sobremesas. "
                    "Qual informação específica você deseja saber? (preços, ingredientes, etc.)")
    elif 'status do pedido' in incoming_msg:
        response = ("Para verificar o status do seu pedido, por favor, forneça o número do pedido ou o nome associado ao pedido.")
    elif 'promoções' in incoming_msg:
        response = ("Atualmente, temos as seguintes promoções: 20% de desconto em pizzas grandes, e uma sobremesa grátis em pedidos acima de R$80.")
    elif 'outras dúvidas' in incoming_msg:
        response = ("Pode me informar qual é a sua dúvida? Farei o meu melhor para ajudar. Se necessário, encaminharei você para um atendente.")
    else:
        response = ("Olá! Bem-vindo à [Nome da Pizzaria]. Sou o assistente virtual. Como posso ajudar você hoje?")

    # Envia a resposta de volta ao usuário
    client.messages.create(
        body=response,
        from_=TWILIO_PHONE_NUMBER,
        to=from_number
    )

    logging.info(f"Sent response: {response} to {from_number}")

    log_message(from_number, incoming_msg, response)

    return jsonify({"status": "success"})

if __name__ == '__main__':
    init_db()
    app.run(port=5000)
