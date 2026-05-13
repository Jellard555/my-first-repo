#以数据为中心，统一存取
class UserRepository:
    def __init__(self):
        self.db = {"1":"kobe","2":"james"}
    def get(self,id):
        return self.db.get(id,"no exists")

repo = UserRepository()
print(repo.get("3"))