#Below are some examples about the features of OOP in Python
#Encapsulation(封装)
class Student:
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score
    def get_name(self):
        return self.name
    def get_age(self):  #如果没有get_age，age这个属性可以在外界被更改

        return self.age
    def get_score(self,new_score):
        if 0 <= new_score <= 100:
            self.score = new_score
        else:
            print("fail")
    def show_info(self):
        print(f"{self.name}{self.age}{self.score}")
stu = Student("jjj",45,56)
stu.show_info()


#Inheritance(继承)
class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def eat(self):
        print(f"{self.name} is eating")
class Student1(Person):
    def __init__(self,name,age,score):
        super().__init__(name,age)
        self.score = score
    def eat(self):
        super().eat()
        print(f"{self.name} is trying to get {self.score}")
class Teacher(Person):
    def __init__(self,name,age,subject):
        super().__init__(name,age)
        self.subject = subject
    def teach(self):
        print(f"{self.name} is teaching {self.subject}")


stu = Student1("小红", 17, 88)
stu.eat()  # 输出：小红正在吃饭 → 小红吃完饭后要写作业，成绩是88

teacher = Teacher("李老师", 35, "数学")
teacher.eat()   # 继承父类方法，输出：李老师正在吃饭
teacher.teach() #