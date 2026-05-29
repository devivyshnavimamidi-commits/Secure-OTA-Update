number=int(input("enter a number"))
print("it is a even number"if number%2==0 else "it is a odd number")

number1=int(input("enter a number1:"))
number2=int(input("enter a number2:"))
print(f"{number1} is greater number"if number1>number2 else f"{number2} is greater number")

for i in range(21):
    print("vyshnavi",i)

for i in range(1,2):
    print(2,2.5,"vyshnavi",(1,23))
           #or
tuple=(1,2.5,"vyshnavi",(12,45))
for i in tuple:
    print(i,end=" ")

for i in range(10,0,-1):
    print(i,end=" ")

for i in range(25,51):
    if i%2==0:
         print(i,end=" ")


sum=0
for i in range(1,31):
        sum+=i
print(sum)

sum=0
for i in "8521":
       sum+=int(i)
print(sum)

for i in range(1,101) : 
  if i%3==0 and i%5==0:
       print(i,end=" ")

for i in range(1,11):
     print(i**2,end=" ")