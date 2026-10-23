import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost', 5672))
channel = connection.channel()

channel.exchange_declare(exchange='review.events', exchange_type='fanout')
channel.basic_publish(
    exchange='review.events',
    routing_key='',
    body='{"event": "review.published", "rating": 5, "server_id": "999"}'
)
print("SENT: review.published to fanout exchange")
connection.close()