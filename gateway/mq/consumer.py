import pika
import json
import asyncio
import websockets
import threading
import os

RABBITMQ_HOST = os.getenv("RABBITMQ_HOST", "localhost")
GATEWAY_WS_URL = os.getenv("GATEWAY_WS_URL", "ws://localhost:8000/ws")

async def enviar_ws(msg):
    try:
        async with websockets.connect(GATEWAY_WS_URL) as ws:
            print("Consumer conectado ao gateway")
            await ws.send(msg)
            print("Consumer enviou:", msg)
    except Exception as e:
        print("Erro ao enviar:", e)

def executar_async(msg):
    """Executa a função assíncrona em uma nova thread com seu próprio loop de eventos"""
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    try:
        loop.run_until_complete(enviar_ws(msg))
    finally:
        loop.close()

def callback(ch, method, properties, body):
    dados = json.loads(body)
    print("Mensagem recebida do RabbitMQ:", dados)

    evento = dados["evento"]
    payload = dados["dados"]

    if evento == "novo_agendamento":
        texto = f"Novo agendamento: {payload}"
    else:
        texto = f"Agendamento cancelado: {payload}"

    msg = json.dumps({
        "type": "mq_event",
        "evento": evento,
        "dados": payload,
        "texto": texto,
        "from_rabbitmq": True,
        "new_notification": True
    })

    # Executa a função assíncrona em uma thread separada
    thread = threading.Thread(target=executar_async, args=(msg,))
    thread.start()

def main():
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(RABBITMQ_HOST)
    )
    channel = connection.channel()

    channel.queue_declare(queue='agendamentos')

    channel.basic_consume(
        queue='agendamentos',
        on_message_callback=callback,
        auto_ack=True
    )

    print("Consumidor esperando mensagens...")
    channel.start_consuming()

if __name__ == "__main__":
    main()