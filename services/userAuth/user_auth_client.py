import user_auth_pb2
import user_auth_pb2_grpc
import profile_pb2_grpc
import profile_pb2

import grpc

# main entrypoint of the system. user logs in or signs up from the client


def run():
    account_exist = input("Already have and account? y/n:")
    email = input("Input email please: ")
    password = input("Password: ")
    # if the user already exists, we request the user-auth service to authenticate
    # the user credentials. Else, we register the user using profile service. Here, I am
    # chanelling two services using gRPC.
    if account_exist == 'y':
        print("Authenticating user .....")
        with grpc.insecure_channel('localhost:50051') as channel:
            stub = user_auth_pb2_grpc.UserAuthStub(channel)
            response = stub.AuthenticateUser(user_auth_pb2.AuthenticationRequest(email=email, password=password))
        print("Success: ", response.success)
        print("Message: ", response.message)

    elif account_exist == 'n':
        print("Will try to register user ...")
        with grpc.insecure_channel('localhost:50052') as channel:
            stub = profile_pb2_grpc.ProfileStub(channel)
            response = stub.RegisterProfile(profile_pb2.RegisterProfileRequest(email=email, password=password))
        print("success", response.success)
    else:
        pass


if __name__ == '__main__':
    run()
