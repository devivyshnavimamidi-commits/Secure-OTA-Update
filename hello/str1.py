str="we is good in eating"
print(str)
print("-"*28)
print(str.replace("is","are"))

a=input("enter any sentence")
print(a.title())

a=input("enter any sentence")
print(a.upper()) 

a=input("enter any sentence")
print(a.lower()) 

word=input("enter any word")
char="aeiouAEIOU"
count=0
for i in word:
 if i in char:
    count+=1
    print(count)

b=input("enter a sentence")
print(len(b))
word=b.strip()
print(len(word))

a=input("enter any sentence")
b=input(("enter any word"))
if a.endswith(b):
    print("Yes")
else:
    print("No")

a=input("enter any word")
if a==a[::-1]:
    print(f"{a} is a palindrom")
else:
    print(f"{a} is not a palindrom")

a=input("enter any sentence")
print(a.capitalize())

a=input("enter any sentence")
b=input(("enter any word"))
if a.startswith(b):
    print("Yes")
else:
    print("No")

