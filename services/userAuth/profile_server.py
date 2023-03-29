from concurrent import futures
import grpc
import profile_pb2
import profile_pb2_grpc
import time
from tinydb import TinyDB

import pika
import sys, os


# start the service during user registration

class ProfileService(profile_pb2_grpc.ProfileServicer):

    def RegisterProfile(self, request, context):
        db = TinyDB('users.json')
        db.insert({'email': request.email, 'password': request.password})
        response = profile_pb2.RegisterResponse(success=True)

        # we then publish user registry event to rabbit mq to trigger the subscribers
        # emailing service in this case. Email service subscribes to this service.
        connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
        channel = connection.channel()
        channel.queue_declare(queue='register')
        channel.basic_publish(exchange='', routing_key='register', body=request.email)
        connection.close()
        return response


def serve():
    port = '50052'
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    profile_pb2_grpc.add_ProfileServicer_to_server(ProfileService(), server)
    server.add_insecure_port('[::]:' + port)
    server.start()
    print("profile server started...")
    time.sleep(5)
    server.wait_for_termination()


if __name__ == '__main__':
    try:
        serve()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
