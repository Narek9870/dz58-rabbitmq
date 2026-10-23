import pika
import sys

message_text = ' '.join(sys.argv[1:]) or 'Task: booking.confirmed..'
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost', 5672))
channel = connection.channel()

channel.queue_declare(queue='ikbo-63-23_zhulev', durable=True)
channel.basic_publish(
    exchange='',
    routing_key='ikbo-63-23_zhulev',
    body=message_text,
    properties=pika.BasicProperties(delivery_mode=pika.spec.PERSISTENT_DELIVERY_MODE)
)
print(f"SENT: {message_text}")
connection.close()