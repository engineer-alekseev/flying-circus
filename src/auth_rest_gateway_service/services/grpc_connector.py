import grpc
from proto import  auth_pb2_grpc
from config import AUTH_GRPC_CHANNEL


def get_grpc_stub():
    channel = grpc.insecure_channel(AUTH_GRPC_CHANNEL)
    stub = auth_pb2_grpc.AuthenticationStub(channel)
    yield stub
    
