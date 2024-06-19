import datetime
import logging

import grpc

from concurrent import futures

import hello_pb2_grpc
import hello_pb2


class Greeter(hello_pb2_grpc.GreeterServicer):

    def SayHello(self, request, context):
        name = request.name
        year = request.year
        age = datetime.datetime.now().year - year
        return hello_pb2.HelloReply(message=f"Nice to know you {name}", age=age)


def server_start():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=5))
    hello_pb2_grpc.add_GreeterServicer_to_server(Greeter(), server)
    server.add_insecure_port('[::]:50000')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    server_start()
