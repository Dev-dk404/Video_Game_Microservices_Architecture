# Copyright 2015 gRPC authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""The Python implementation of the GRPC helloworld.Greeter server."""

import logging
from concurrent import futures

import grpc
from tinydb import TinyDB, Query

import user_auth_pb2
import user_auth_pb2_grpc
import sys,os


# start the service during user authentication

class UserAuth(user_auth_pb2_grpc.UserAuthServicer):

    def AuthenticateUser(self, request, context):
        User = Query()
        db = TinyDB('users.json')
        result = db.search((User.email == request.email) & (User.password == request.password))
        if len(result) > 0:
            response = user_auth_pb2.AuthenticationResponse(success=True, message="User Authenticated")
        else:
            response = user_auth_pb2.AuthenticationResponse(success=False, message="User  not authenticated")
        return response


def serve():
    port = '50051'
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    user_auth_pb2_grpc.add_UserAuthServicer_to_server(UserAuth(), server)
    server.add_insecure_port('[::]:' + port)
    server.start()
    print("Server started, listening on " + port)
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
