#Model:数据 + 逻辑
class Model:
    def get_data(self):
        return "info:"

#界面展示
class View:
    def show(self,data):
        print("=======show=======")
        print(data)
        print("==================")

# 调度
class Controller:
    def __init__(self):
        self.model = Model()
        self.view = View()

    def handle_request(self):
        data = self.model.get_data()
        self.view.show(data)

if __name__ == "__main__":
    print("open the interface")
    controller = Controller()
    controller.handle_request()