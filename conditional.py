name="vyshnavi"
print(f"my name is {name}, i am learning python by pruthvi sir")

my_list=["apple","banana","grapes","orange"]
print("watermelon" in my_list)
print("grapes" in my_list)

age=int(input("enter the age"))
if age>59 :
    print(f"this {age} age people get pension")
else :
    print(f"this {age} age people does not get pention")

number=int(input("enter the number"))
if number>0 :
    print(f"{number} is positive ")
elif number<0 :
    print(f"{number} is negative")
else :
    print(f"{number} is zero")

a=int(input("enter the number a"))
b=int(input("enter the number b"))
operators= input("enter the operators (+,-,*,/)")
if operators == "+":
    print(a+b)
elif operators == "-":
    print(a-b)
elif operators=="*" :
    print(a*b)
elif operators == "/" :
    print(a/b)
else :
    print("invalid operators")

a=int(input("enter the number a"))
b=int(input("enter the number b"))
c=int(input("enter the number c"))
if (a>=b) and (a>=c):
    print(f"{a} is big")
elif (b>=a) and(b>=c):
    print(f"{b} is big")
else :
    print(f"{c} is big")

username=input("enter your username ")
password=input("enter your password")
if username =="mahesh" :
    if password == "6789":
        print(f"login successful")
    else :
        print(f"worng password")
else :
   print("invalid username")