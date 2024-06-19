import logging

import grpc

import hello_pb2_grpc
import hello_pb2


def run():
    with grpc.insecure_channel("localhost:50000") as channel:
        stub = hello_pb2_grpc.GreeterStub(channel)
        response = stub.SayHello(hello_pb2.HelloRequest(name="Emanuel"))
        print(f'Response from server: {response}')


if __name__ == '__main__':
    logging.basicConfig()
    run()
