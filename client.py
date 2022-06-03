import todo_pb2_grpc
import todo_pb2
import grpc

def run():
    try:
        with grpc.insecure_channel('localhost:8080') as channel:
            stub = todo_pb2_grpc.TodoStub(channel)
            todo_request = todo_pb2.TodoItem(id = 1, text = "new todo")
            reply = stub.createTodo(todo_request)
            print("Response Received:")
            print(reply)

            todos_request = todo_pb2.TodoRequest()
            reply = stub.readTodos(todos_request)
            print("Response Received:")
            print(reply)
    except error:
        print(error) 


if __name__ == "__main__":
    run()