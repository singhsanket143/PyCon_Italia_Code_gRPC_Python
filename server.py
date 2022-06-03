from concurrent import futures
import grpc
import todo_pb2
import todo_pb2_grpc

class TodoService(todo_pb2_grpc.TodoServicer):

    def __init__(self):
        self.todos = []

    def createTodo(self, request, context):
        raise Exception('Not Implemented')
    
    def readTodos(self, request, context):
        raise Exception('Not Implemented')


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    todo_pb2_grpc.add_TodoServicer_to_server(TodoService(), server)
    server.add_insecure_port("localhost:8080")
    server.start()
    server.wait_for_termination()

if __name__ == "__main__":  
    serve()