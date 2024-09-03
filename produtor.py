import pika
from termcolor import colored


connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(queue='minha_fila')

channel.basic_publish(
    exchange='',
    routing_key='minha_fila',
    body='Olá essa é uma nova mensagem novaaa!'
)

print(colored('[x] Mensagem enviada para fila: minha_fila','white','on_green'))

connection.close()