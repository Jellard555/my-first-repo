#多个实例共享一个状态，一个改变，全部改变
class Borg:
    _shared_state = {}

    def __init__(self):
        self.__dict__ = self._shared_state


b1 = Borg()
b2 = Borg()

b1.name = "shared title"
b1.data = 100

print(b2.name)
print(b2.data)

b2.data = 666
print(b1.data)

print(b1 is not b2)