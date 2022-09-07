import pika

AMQP_URL = "amqps://rforetzs:WB23MdLWPBx7TgU4WMGWceaBYQjiBACE@rattlesnake.rmq.cloudamqp.com/rforetzs"
params = pika.URLParameters(AMQP_URL)
connection = pika.BlockingConnection(params)

channel = connection.channel()


def publish():
    channel.basic_publish(exchange="", routing_key="main", body="hello")
