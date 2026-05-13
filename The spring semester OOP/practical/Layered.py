#分层架构，按层级调用，上层只依赖下层

#1
class Physicallayer:
    def send(self,data):
        return f"[物理层]发送信号：{data}"
#2  
class DataLinkLayer:
    def __init__(self):
        self.physical = Physicallayer()
    def send(self,data):
        return self.physical.senf(f"[数据]封锁帧：{data}")
#3  
class NetworkLayer:
    def __init__(self):
        self.datalink = DataLinkLayer()
    def send(self,data):
        return self.datalink.send(f"[网络层]路由：{data}")
    
net = NetworkLayer()
print(net.send("hello"))