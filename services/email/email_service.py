import pika
import sys
import os


# email service prints out "email sent" message to the terminal for now
# it is only triggered once the user is registered, message received through rabbitmq.


def callback(ch, method, properties, body):
    print("Email sent to ", body.decode())


def main():
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()
    channel.queue_declare(queue='register')

    channel.basic_consume(queue='register', on_message_callback=callback, auto_ack=True)
    channel.start_consuming()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
