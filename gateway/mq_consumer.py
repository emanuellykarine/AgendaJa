import asyncio
import json

from mq.runner import start_consumer

def start_mq_consumer(loop, broadcast_message):
    def callback(_ch, _method, _properties, body):
        dados = json.loads(body)
        msg = json.dumps(dados)

        # envia para o loop do FastAPI
        asyncio.run_coroutine_threadsafe(
            broadcast_message(msg),
            loop
        )

    start_consumer(callback)
