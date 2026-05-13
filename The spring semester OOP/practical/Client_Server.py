#客户端请求，服务器响应
class Server:
    def response(self):
        return "返回数据"
class Client:
    def __init__(self,server):
        self.server = server
    def request(self):
        print("客户端发起请求")
        print(self.server.response())

server = Server()
client = Client(server)
client.request()