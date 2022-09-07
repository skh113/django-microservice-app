import pika

AMQP_URL = "amqps://rforetzs:WB23MdLWPBx7TgU4WMGWceaBYQjiBACE@rattlesnake.rmq.cloudamqp.com/rforetzs"
params = pika.URLParameters(AMQP_URL)
connection = pika.BlockingConnection(params)

channel = connection.channel()

channel.queue_declare(queue="admin")


def callback(ch, method, properties, body):
    print("Received in admin")
    print(body)


channel.basic_consume(queue="admin", on_message_callback=callback, auto_ack=True)
print("Started Consuming")

channel.start_consuming()

channel.close()
