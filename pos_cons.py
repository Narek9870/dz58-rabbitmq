import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost', 5672))
channel = connection.channel()
channel.exchange_declare(exchange='review.events', exchange_type='fanout')

result = channel.queue_declare(queue='', exclusive=True)
queue_name = result.method.queue
channel.queue_bind(exchange='review.events', queue=queue_name)

def process_message(channel, method, properties, body):
    print(f"RECEIVED via FANOUT: {body.decode()}")

channel.basic_consume(queue=queue_name, auto_ack=True, on_message_callback=process_message)
print(f"Waiting for fanout messages in queue {queue_name}...")
channel.start_consuming()