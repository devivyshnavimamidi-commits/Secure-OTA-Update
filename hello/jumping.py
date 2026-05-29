number=10
while number:
 number<=1
 print(number,end=" ")
 number-=1



number=24
while number<=50:
  if number%2!=0:
   print(number,end=" ")
  number+=1



sum=0
for i in range(1,31):
  sum+=i
print(sum,end=" ")   

sum=0
number=1
while number<=30:
 sum+=number
 number+=1
print(sum,end=" ")



n=int(input("enter a number"))
fact=1
for i in range(1,n+1):
    fact*=i
print(fact,end=" ")

while True:
   number=int(input("enter a number"))
   if number>0:
    print(f"{number} is positive")
   else :
    print(f"{number} is a negitive")
    break


for i in range(1,6):
 password=input("enter your password")
 if password=="123":
        print(f"login successful")
        break
 else:
        print(f"login failed")
else :
   print("you have crossed your attempts, logione failed")

    