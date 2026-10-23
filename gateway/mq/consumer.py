import json
import asyncio
import websockets
import threading
import os

from runner import start_consumer

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
    print("Consumidor esperando mensagens...")
    start_consumer(callback)

if __name__ == "__main__":
    main()
