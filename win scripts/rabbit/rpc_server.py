# _*_ coding:utf-8 _*_
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='rpc_queue')

def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

def on_request(ch,method,props,body):
    n = int(body)
    print "[.]fib(%s)" %(n,)

    response = fib(n)

    ch.basic_publish(exchange='',
                     routing_key=props.reply_to,
                     propertes=pika.BasicProperties(correlation_id= props.correlation_id),

                         body=str(response)
                     )
    ch.basic_ack(delivery_tag = method.delivery_tag)