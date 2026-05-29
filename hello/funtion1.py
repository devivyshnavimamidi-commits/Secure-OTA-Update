def greet():
    print("Hello,india")
greet()

def welcome_user(name):
    print(f"welcome,{name}!")
welcome_user("vyshnavi")
welcome_user("tanuja")
welcome_user("surya")

def order(food="pizza"):
    print(f"you ordered : {food}")
order()
def order(food="pizza"):
    print(f"you ordered : {food}")
order("burger")

def sum_all(*args):
    sum=0
    for i in args:
     sum+=i
    print(f"sum is :{sum}")     
sum_all(1,2,3)
sum_all(10,20)
sum_all()

def user_info(**kwargs):
    print(kwargs)
user_info(name="vyshnavi",age=19,marks=90)

def sum(a,b):   #formal parameters or perameters or formal arguments
    print(a+b)
sum(4,5)        #arguments or actual perameters or actual arguments

def display_info(name,age):                  #formal parameters or perameters or formal arguments
    print(f"{name} is {age} years old.")
display_info("ramya",12)                     #arguments or actual perameters or actual arguments

def calculate_area(length,width):
   area=length*width
   print(area)
calculate_area(length=int(input("enter the length of a rectangle")),width=int(input("enter a width of a rectangle")))

