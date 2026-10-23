import pika
import time

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost', 5672))
channel = connection.channel()
channel.queue_declare(queue='ikbo-63-23_zhulev', durable=True)

def process_message(channel, method, properties, body):
    print(f"RECEIVED: {body.decode()}")
    time.sleep(body.count(b'.'))
    print("INFO: Task Done")
    channel.basic_ack(delivery_tag=method.delivery_tag)

channel.basic_qos(prefetch_count=1)
channel.basic_consume(queue='ikbo-63-23_zhulev', on_message_callback=process_message)
print('Waiting for tasks...')
channel.start_consuming()