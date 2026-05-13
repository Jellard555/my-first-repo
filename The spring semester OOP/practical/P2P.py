#每个节点既是客户端也是服务端
class Peer:
    def __init__(self,name):
        self.name = name
    def send(self,peer,msg):
        print(f"{self.name}→{peer.name}:{msg}")
p1 = Peer("Pa")
p2 = Peer("Pb")
p1.send(p2,"w1")
p2.send(p1,"w2")