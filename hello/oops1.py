class student():
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display_info(self):
        print(f"the student name is {self.name} and age {self.age}")
student1=student("vyshnavi",19)
student1.display_info()

class calculater():
    def __init__(self,a,b):
      self.a=a
      self.b=b
    def add(self):
        c=self.a+self.b
        print(f"the sum is {c}")
    def sub(self):
        c=self.a-self.b
        print(f"the sub is {c}")
    def mul(self):
        c=self.a*self.b
        print(f"the mul is {c}")
    def div(self):
        c=self.a/self.b
        print(f"the div is {c}")
operator=calculater(6,8)
operator.add()
operator.sub()
operator.mul()
operator.div()

class rectangle():
    def __init__(self,l,w):
        self.l=l
        self.w=w
    def area(self):
        area=self.l*self.w
        print(f"area of rectangle is {area}")
    def perimeter(self):
        perimeter=2*(self.l+self.w)
        print(f"peimeter of rectangle is {perimeter}")
result=rectangle(4,2)
result.area()
result.perimeter()

class employee():
    def __init__(self,name,position,salary):
        self.name=name
        self.position=position
        self.salary=salary
    def display(self):
        print(f"the employee name is {self.name} and position is {self.position} and salary is {self.salary}")
details1=employee("vyshnavi","software employee",6500000)
details2=employee("tanuja","doctor",6000000)
details1.display()
details2.display()

import math
class circle():
    def __init__(self,r):
        self.r=r
    def calculate(self):
        area=math.pi*self.r*self.r
        print(f"area of circle {area}")
        circumference=2*math.pi*self.r
        print(f"circumference of circle is {circumference}")
result=circle(4)
result.calculate()

