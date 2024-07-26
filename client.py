# client.py
import grpc
import greeting_pb2
import greeting_pb2_grpc

def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = greeting_pb2_grpc.GreeterStub(channel)
        response = stub.SayHello(greeting_pb2.HelloRequest(name='World'))
    print("Greeter client received: " + response.message)

if __name__ == '__main__':
    run()
