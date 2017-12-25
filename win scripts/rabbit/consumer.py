# _*_ coding:utf-8 _*_

import pika

connection = pika.BlockingConnection (pika.ConnectionParameters ('localhost'))
channel = connection.channel()

channel.queue_declare(queue='hello',durable=True)
def callback(ch, method, properties, body):
    print(ch,method,properties)
    print(" [x] Received %r" % body)


channel.basic_consume (callback,
                       queue='hello'
                       #no_ack=True
 )
print(' [*] waiting for messages.To exit press CTRL+C')
channel.start_consuming()
