import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost', 5672))
channel = connection.channel()
channel.exchange_declare(exchange='deploy.events', exchange_type='direct')

channel.queue_declare(queue='ikbo-63-23_golovach')
# Подписка на конкретные ключи
channel.queue_bind(exchange='deploy.events', queue='ikbo-63-23_golovach', routing_key='deploy.completed')
channel.queue_bind(exchange='deploy.events', queue='ikbo-63-23_golovach', routing_key='deploy.failed')

def process_message(channel, method, properties, body):
    print(f"RECEIVED [{method.routing_key}]: {body.decode()}")

channel.basic_consume(queue='ikbo-63-23_golovach', auto_ack=True, on_message_callback=process_message)
print('Waiting for direct messages...')
channel.start_consuming()