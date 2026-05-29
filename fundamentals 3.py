number=3.8
print(type(number))
a=int(number)
print(a)
print(type(a))

about={"name":"vyshnavi","study":"b-tech","age":19}
print(about)
print(type(about))

number1=6
print(type(number1))
c=complex(number1)
print(c)
print(type(c))
number=4+5j
print(type(number))
d=(float(number.real),float(number.imag))
print(d)
print(type(d))

number=5
print(str(number))
print(type(str(number)))

in_list=["vyshnavi,8,9,5,4"]
print(tuple(in_list))
in_list=[3,5,6,7,7]
print(set(in_list))
tuple=((int,1),(float,4.6))
print(dict(tuple))

str1="vyshnavi"
str2="tanuja"
print(str1,str2,sep=',')
print(str1+str2)
print(str1+"  "+str2)

name=("vyshnavi"*15)
print(name)

name=input("enter your name")
print(name)

first=input("enter the first number")
second=input("enter the second number")
a=int(first)
print(a)
b=int(second)
print(b)
print(a-b)

