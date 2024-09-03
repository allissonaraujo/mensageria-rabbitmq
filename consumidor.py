import pika
from termcolor import colored

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(queue='minha_fila')

def callback(ch, method, properties, body):
    print(f" [x] Mensagem Recebida: {body.decode()}")

channel.basic_consume(queue='minha_fila', on_message_callback=callback, auto_ack=True)

print(colored(' [*] Esperando por mensagens, aperte control + c para sair','light_blue','on_cyan'))

channel.start_consuming()