#!/usr/bin/env python

# _*_ coding:utf-8 _*_
import pika
import time

connection = pika.BlockingConnection (pika.ConnectionParameters (host='localhost'))

channel = connection.channel ()
channel.queue_declare (queue='task_queue', durable=True)
print('[*] waiting for messages. To exit press ctrl+c')


def callback(ch, method, properties, body):
    print(" [x] Receive %r" % body)
    time.sleep (body.count (b'.'))
    print ("[x] Done")
    ch.basic_ack (delivery_tag=method.delivery_tag)    # 对message进行确认
#若存在多个consumer每个consumer的负载可能不同，有些处理的快有些处理的慢
#RabbitMQ并不管这些，只是简单的以round-robin的方式分配message
#这可能造成某些consumer积压很多任务处理不完而一些consumer长期处于饥饿状态
#可以使用prefetch_count=1的basic_qos方法可告知RabbitMQ只有在consumer处理并确认了上一个message后才分配新的message给他
#否则分给另一个空闲的consumer

channel.basic_qos (prefetch_count=1)
channel.basic_consume(callback,queue='task_queue')

channel.start_consuming()

