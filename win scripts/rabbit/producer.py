# _*_ coding:utf-8 _*_

import pika
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.queue_declare(queue='hello',durable=True)
channel.basic_publish(exchange='',
                      routing_key='hello',
                      body='Hello World')
print("[x] Sent 'Hello world!'")
connection.close()

