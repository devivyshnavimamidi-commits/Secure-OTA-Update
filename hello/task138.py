def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b
def output():
    while True:
        a=float(input("enetr the value of a"))
        b=float(input("enter the value of b"))
        print("1. addition")
        print("2. subtraction")
        print("3. multiplication")
        print("4. division")
        choice=input("enter your choice")
        if choice=="1":
            print(add(a,b))
        elif choice=="2":
            print(sub(a,b))
        elif choice=="3":
            print(mul(a,b))
        elif choice=="4":
            print(div(a,b))
        else:
            print("invalide choice")
            break
output()

a=10            #it is a globle variable
def sum(a,b):
    b=2         # it is a local variable
    c=a+b
    print(c)
sum()           #it is funtion calling

count=40
def modify_count():
    count=60
    print(f"value before calling the funtion {count}")
modify_count()
print(f"value after calling the funtion {count}")

count=30
def modify_count():
    count=80
    print(f"value before calling the funtion {count}")
modify_count()
print(f"value after calling the funtion {count}")

import random
print(random.randint(20,30))

import statistics
data=[1,2,3,4,5]
print(statistics.median(data))


        