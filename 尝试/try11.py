#class Student :
 #   def __init__(self,name,number):
  #      self. name = name
   #     self. number = number
    #    self.grades = {'语文':0,'数学':0,'英语':0}
    #def set_grade(self,course,grade):
     #   if course in self.grades:
      #      self.grades[course] = grade
    #def print_grade(self):
     #   print(f"学生{self.name}(学号：{self.number})的成绩为：")
      #  for course in self.grades:
       #     print(f"{course}:{self.grades[course]}分")
#student1 = Student('zeng',15)
#student1.set_grade("语文",95)
#student1.print_grade()


class Employee:
    def __init__(self,name,id):
        self.name = name
        self.id = id
    def print_info(self):
        print(f'员工名字{self.name}.工号{self.id}')

class FullTimeEmployee(Employee):
    def __init__(self,name,id,monthly_salary):
        super().__init__(name,id)
        self.monthly_salary = monthly_salary
    def calculate_monthly(self):
        return self.monthly_salary
class PartTimeEmployee(Employee):
    def __init__(self,name,id,daily_salary,work_days):
        super().__init__(name,id)
        self.daily_salary = daily_salary
        self.work_days = work_days
    def calculate_monthly(self):
        return self.daily_salary * self.work_days
zhangsan = FullTimeEmployee('zhangsan',10086,400)
lisi = PartTimeEmployee('lisi',555,65,100)
zhangsan.print_info()
lisi.print_info()
print(zhangsan.calculate_monthly())
print(lisi.calculate_monthly())
