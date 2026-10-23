import os

import pika


def start_consumer(callback):
    rabbitmq_host = os.getenv("RABBITMQ_HOST", "localhost")
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host=rabbitmq_host)
    )
    channel = connection.channel()
    channel.queue_declare(queue="agendamentos")
    channel.basic_consume(
        queue="agendamentos",
        on_message_callback=callback,
        auto_ack=True,
    )
    channel.start_consuming()
