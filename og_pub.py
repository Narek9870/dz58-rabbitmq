import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost', 5672))
channel = connection.channel()

channel.queue_declare(queue='ikbo-63-23_ogannisyan')
channel.basic_publish(
    exchange='',
    routing_key='ikbo-63-23_ogannisyan',
    body='{"event": "service.added", "service_id": "123", "name": "Extra Server Slots"}'
)
print("SENT: service.added")
connection.close()