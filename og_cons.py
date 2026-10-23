import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost', 5672))
channel = connection.channel()
channel.queue_declare(queue='ikbo-63-23_ogannisyan')

def process_message(channel, method, properties, body):
    print(f"RECEIVED: {body.decode()}")

channel.basic_consume(queue='ikbo-63-23_ogannisyan', auto_ack=True, on_message_callback=process_message)
print('Waiting for messages...')
channel.start_consuming()