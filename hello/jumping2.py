for i in range(1,21):
    if i==5:
     continue
    print(i,end=" ")

for i in range(50,301):
   if i%2!=0:
      continue
   print(i,end=" ")
          
list=[1,3,5,6,7,8,4,9]
number=int(input("enter a number"))
for i in list:
    if i==number:
     print(f"{number} is found")
     break
else:
   print(f"{number} is not found")



for i in range(1,101):
   if i%7==0 and i%5==0 :
      print(i,end=" ")
      break

letter=input("enter any name")
vowel="a,e,i,o,u,A,E,I,O,U"
for i in letter:
    if i in vowel:
        continue
    print(i,end=" ")
   