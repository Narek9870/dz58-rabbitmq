import pika
import sys

routing_key = sys.argv[1] if len(sys.argv) > 1 else 'deploy.completed'
message = '{"server_ip": "192.168.1.1"}' if routing_key == 'deploy.completed' else '{"error": "Timeout"}'

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost', 5672))
channel = connection.channel()

channel.exchange_declare(exchange='deploy.events', exchange_type='direct')
channel.basic_publish(
    exchange='deploy.events',
    routing_key=routing_key,
    body=message
)
print(f"SENT: {routing_key} -> {message}")
connection.close()