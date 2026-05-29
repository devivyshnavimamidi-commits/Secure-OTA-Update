numb=input("enter a value")
if numb.isdigit():
    print(int(numb)*2)
else:
    print(f"{numb} is not a valid value")
print()

string="Mahesh123"
for i in string:
    if i.isdigit():
        print(i,end=" ")

name=input("enter a name")
checkname=name.isalpha()
print(checkname)

list=["Mahesh","pavan123","suresh","ch3rry"]
for i in list:
    if i.isalpha():
       print(i)
    
username=input("enter your username:")
print(f"accepted" if username.isalnum() else "please check your username")
  
list1=["hgfh","kjgcdw678","hegjhw","94875"]
my_list=[]
for i in list1:
    if i.isalnum():
        print(i,end=" ")
    
name=input("enter your name")
age=input("your age")
print("hello..{}. you are {} years old".format(name,age))

sentence="today-i-went-to-ncc-i-got-fever-and-pains"
print(sentence.split("-"))

list=["and","today","vinayaka","nimarjanam"]
newlist=" ".join(list)
print(newlist)

input="and i have focused in python cource"
output=input.split()
print(output)
print("-".join(output))