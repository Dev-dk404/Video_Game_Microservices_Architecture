# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import profile_pb2 as profile__pb2


class ProfileStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.RegisterProfile = channel.unary_unary(
                '/profile.Profile/RegisterProfile',
                request_serializer=profile__pb2.RegisterProfileRequest.SerializeToString,
                response_deserializer=profile__pb2.RegisterResponse.FromString,
                )


class ProfileServicer(object):
    """Missing associated documentation comment in .proto file."""

    def RegisterProfile(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ProfileServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'RegisterProfile': grpc.unary_unary_rpc_method_handler(
                    servicer.RegisterProfile,
                    request_deserializer=profile__pb2.RegisterProfileRequest.FromString,
                    response_serializer=profile__pb2.RegisterResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'profile.Profile', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Profile(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def RegisterProfile(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/profile.Profile/RegisterProfile',
            profile__pb2.RegisterProfileRequest.SerializeToString,
            profile__pb2.RegisterResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)