#task 2
#print your name and your father name
# print("surya prakash")
# print("devi vyshnavi")

#syntax for print statement
#print()         #it is used to print information

#print text
#print("today we are discussing fundamentels of python")   #for text we should keep ""

#print values
#print(10+25)     #for values no need to keep ""

#print hello, world! statement
#print("hello, world!")

#print this is my first program
#print("this is my first program")

#------->comment-------->

#select lines and ctrl+?-----> single line

#below code is used to perform addition operation
# number1=5     #variable 1
# number2=10    #variable 2
# print(number1+number2)

#-------> single line comment

'''
i have taken two variables
and i assigned values to those variables
and i perform addition operation by using + operation

'''

#'''   '''   (or)   """    """ -----> multi line comment

#------->variable------->

#variable is a container that store the value
#syntax:variable name=value
#example
# name="vyshanvi"
# age=25
# print(name)
# print(id(name))         #--------->id-->address
# print(age)
# print(id(age))

#python is dynamic type
#int age=5 ----> we can not declare like this due to it is a dynamic type
#we no need to declare the type 

#c is static type 
#int age=5 ---->we can declare like this in c and some other languages
#we should declare the type of value we assigned 

#writing the variable names
# Weight=3.5
# print(Weight)   #we can start write with capital letter
# _weight=3.5
# print(_weight)  #we can start write with underscore _
# age=35
# print(age)      #we can start write with small letters
# ag1e=35
# print(ag1e)     #we can write numbers in middle of variable name
# ag_e=35
# print(ag_e)     #we can write underscore_ in middle of variable name
# ag1_e=35
# print(ag1_e)    #we can write both numbers and underscore in middle of variable name
# ag$e=35
# print(ag$e)     #we can not use spical symbols

#case sensitive
# name="vyshanvi"
# Name="tanuja"
# NAME="surya prakash"
# NAme="anu radha"
# print(NAME)

#------->keywords-------->

#keywords cannoot use like variable name
# example:if =25
# print(if)  --->if is a keyword not use like a variable name
#we an write 
# _if=25
# print(_if)

#keyword code
# import keyword
# print(keyword.kwlist)

#------>variable cases------>

#camelCase
# userName="vyshanvi"
# print(userName)

# #snake_case
# user_name="vyshanvi"
# print(user_name)

# #PascalCase
# UserName="vyshanvi"
# print(UserName)

#-------->data types-------->

# numeric--->integer
#        --->float
#        --->complex number
# dictionary
# boolean
# set
# sequence type--->string
#              --->tuple
#              --->list
#sequence type have indexing,slicing,ordered

#------>integer------>
#int is a  positive or negetive

# age=30
# print(age)
# print(type(age))

# age=-75
# print(age)
# print(type(age))

# number=0
# print(type(number))

 #---->float----->
#float is a decimal point

# age=30.5
# print(age)
# print(type(age))

# age=-80.5
# print(age)
# print(type(age))

# age=0.0
# print(age)
# print(type(age))

# number=4.3
# print(id(number))

#------->string------>
#'  ' or "  "or "'  '" we use
# example : "pythonlife", "123"

# name="vyshanvi"
# print(name)
# print(type(name))
# print(id(name))
# #  (or)
# name='''tanuja'''
# print(name)
# print(type(name))
# print(id(name))

# number="23"
# print(type(number))

# text="python vyshnavi's session"
# print(text)

# text="""today we are discussing 
#         about string topic"""
# print(text)

# text='python"vyshnavi"session'
# print(text)

# a=15
# b=20
# print(a,b)

# a=15
# b=20
# print(a,b,sep=",")

# task 4
#create a variable called name and assign your name to it. print the value
# name="vyshnavi"
# print(name)

# task 5 
# create a variable city and assing your favorite city name. print it
# city="u.s.a"
# print(city)

# task 6
# create variable of the following types:
# string
# integer
# float
# print each variable and use type()to print its data type.
# name="vyshnavi"
# print(name)
# print(type(name))
# number=19
# print(number)
# print(type(number))
# number=45.8
# print(number)
# print(type(number))

# task 7
# using single line comments and multiline comments write a python program
# name1="vyshnavi"       #----->single line comment
# name2="tanuja"
# print(name1,name2)

'''my name is vyshnavi and i am learning 
python in 2nd year'''       
# '''  ''' (or) """ """-----> multi line comment

# task 8
# x=100
# y=50
# display output like these->100,50
# x=100
# y=50
# print(x,y,sep=",")

#------->complex number----->
# realpart+imaginary part
# example:2+3j

# number=3+5j     #we should use only j
# print(number)
# print(type(number))

# number=4+j5    #----->you should not write like this 
# print(number)
# print(type(number))

# number1=4+5j
# number2=5+4j
# print(number1+number2)

# formula---->I=V/R
# I---->current,V----->voltage,R----->resistence
# R=3+4j
# V=220
# I=V/R
# print(I)

#--------> boolean-------->
# gives true or false

# print(5<3)
# print(type(5<3))

# number=0
# print(bool(number))    if 0 it will give false

# number=255
# print(bool(number))     if non-zero it will give true

# name=""
# print(bool(name))    #empty string will give false

# name=" "
# print(bool(name))    #space also consider as string then it will give true

# a complex number eavaluates to false if both real and imaginary part is zero
# number=3+5j
# print(bool(number))
# number=0+4j
# print(bool(number))
# number=5+0j
# print(bool(number))
# number=0+0j
# print(bool(number))
# number=3*0
# print(bool(number))

# n----->numeric---->int,float,complex numbers
# t----->tuple
# s----->string
# these are immutable--->not changable
'''
immutable means once a number object is created
its value cannot be changed. if you change it
python actually creates a new object in memory'''

# integer---->immutable
# number=5
# print(id(number))     #different address is immutable
# number=number+2
# print(id(number))     #same address is mutable

# float----->immutable
# number=5.3
# print(id(number))
# number=number+2.3
# print(id(number))

# complex number--->immutable
# number=3+5j
# print(id(number))
# number=number*3
# print(id(number))

# tuple---->immutable
# tuple=(2,5,6)
# tuple[0]=4
# print(tuple)

# tuple=(1,2,3)
# print(id(tuple))
# tuple=tuple+(4,5,6)
# print(id(tuple))

# string---->immutable
# text="hello"
# print(id(text))
# text=text+"word"
# print(id(text))

# string concatination
# name1="python"
# name2="life"
# print(name1+name2)

# boolean--->immutable
# number=True
# print(id(number))
# number=not number
# print(id(number))

# list---->mutable
# tuple=[2,5,6]
# tuple[0]=4
# print(tuple)

# list1=[1,2,3]
# print(list1)
# print(id(list1))
# print()
# list1.append(5)
# print(list1)
# print(id(list1))

# --------->list--------->
# mutable----->we can change
# elements can be of different data types
# duplicates are allow
# list is ordered
# [] are used
# example:my_list=[2,3.4,"vyshnavi",true]

# number=[]
# print(type(number))

# my_list=[2,3.5,"vyshnabvi",True,[1,"tanuja"],2+3j,(2,5)]
# print(my_list)

# list1=[1,2,3]
# print(list1)
# print(id(list1))
# print()
# list1.append(5)
# print(list1)
# print(id(list1))

# my_list=[2,5,2,5,2,5,2,5]
# print(my_list)

# -------->tuple------->
# immutable------->we cannot change
# elements can be different data types
# duplicates are allow
# ()are used
# tuple is ordered
# example:my_tuple=(2,3.5,2,3,2)

# number=()
# print(type(number))

# a=5,6,3+5j
# print(a)
# print(type(a))

# number=(5)
# print(type(number))

# number=(5,)
# print(type(number))

# my_tuple=(92,3.5,"vyshanvi",True,2+5j,[2,3],(2,4))
# print(my_tuple)

# my_tuple=(2,35,6)
# my_tuple[1]=7
# print(my_tuple)

# number=(2,3,4,42,2,23,3,2,3,2)
# print(number)

# ------->set--------->
# mutable-------->we can change
# set is unordered
# {} are used
# duplicates are not allow
# it allow only immutable data type

# my_set={2,2.3,"vyshnavi",True,3+5j,(2,4)}
# print(my_set)

# my_set={2,2.3,"vyshnavi",True,3+5j,(2,4)}
# my_set.add("tanuja")
# print(my_set)

# my_set={2,2.3,"vyshnavi",True,3+5j,(2,4),[2,4]}
# print(my_set)

# my_set={2,2.3,"vyshnavi",True,2,2,3+5j,(2,4)}
# print(my_set)

# numbers={2,3,5,1,2,True,5,False,2,0}
# print(numbers)

# numbers={2,3,5,(2,3),45}
# print(numbers)

# numbers={2,3,5,(2,3),(2,3),45}
# print(numbers)

# task 9
# take any two complex numbers perform addition
# number1=5+7j
# number2=6+3j
# print(number1+number2)

# task 10
# write a program to check if a number is positive
# number=44
# print(number>0)

# task 11
# create a set with duplicate values and observe the result
# my_set={2,3,2,3,2,32,3,2,3,2,3,2}
# print(my_set)

# task 12
# create a tuple with mixed data types and display the output
# my_tuple=(2,2.3,4+5j,(5,6),[5,7],True)
# print(my_tuple)

# task 13
# create a list of 5 strings and display the output
# my_list=["vyshanvi","tanuja","surya prakash","anu radha"]
# print(my_list)

# --------->dictionary------->
# it is a key:value pairs
# dictionary is a ordered collection of key:value pairs
# mutable---->we can change
# {} are used
# keys should be immutable
# keys in dictionary must be unique,if duplicate keys are used it will override the existing value
# values can be of any type
# example:my_dictionary={"name":"vyshnavi","age":19,"city":"perumallapuram"}
# key+value--->item

#number={}
# print(type(number))

# number={5}
# print(type(number))

# number={"name":"vyshnavi","age":19}
# print(type(number))

# user_data={"name":"vyshnavi","age":19}
# print(user_data)
# user_data["city"]="perumallapuram"
# print(user_data)

# user_data={"name":"vyshnavi","age":19,(2,3):5}
# print(user_data)

# user_data={"name":"vyshnavi","age":19,"name":"tanuja"}
# print(user_data)      #override the key value and give last name in output

# number=set()
# print(type(number))

# number=set([2,5,6])
# print(number)

# --------->type convertion------------->
# int----->float

# age=35
# print(age)
# print(type(age))
# b=float(age)
# print(b)
# print(type(b))

# # float------->int

# weight=25.3
# print(weight)
# print(type(weight))
# c=int(weight)
# print(c)
# print(type(c))

# int------->string
# age=40
# print(type(age))
# c=str(age)
# print(c)
# print(type(c))

# string------>int
# age="40"              #only numerical can convert not a text
# print(type(age))
# c=int(age)
# print(c)
# print(type(c))

# float-------->string
# weight=25.3
# print(weight)
# print(type(weight))
# c=str(weight)
# print(c)
# print(type(c))

# # string------>float
# weight="25.3"
# print(weight)
# print(type(weight))
# c=float(weight)
# print(c)
# print(type(c))

# int----->complex
# number=5
# c=complex(number)
# print(c)

# number1=5
# number2=3
# print(complex(number1,number2))

# # complex------>int
# number=3+5j
# c=int(number.real)
# print(c)
# c=int(number.imag)
# print(c)

# number=3+5j
# print(int(number.real),int(number.imag))

# float------>complex
# number=5.3
# c=complex(number)
# print(c)

# number1=5.3
# number2=6.7
# c=complex(number1,number2)
# print(c)

# complex---->float
# number=3+5j
# print(float(number.real),float(number.imag))

# string------>complex
# number="2"
# c=complex(number)
# print(c)

# number="2+3j"
# print(complex(number))

# number="vyshavi"          #text cannot change
# print(complex(number))

# number1=2
# number2=5
# print(complex(int(number1),int(number2)))

# complex------>string
# number=3+5j
# print(type(number))
# c=str(number)
# print(c)
# print(type(c))

# boolean---->int
# number1=True
# number2=False
# print(int(number1),int(number2))

# boolean----->float
# number1=True
# number2=False
# print(float(number1),float(number2))

# boolean------->string
# number1=True
# number2=False
# print(str(number1),str(number2))

# boolean----->complex
# number1=True
# number2=False
# print(complex(number1),complex(number2))

# iterables---->cannot be converted (loop)------>list,tuple,dictionary,set
# a=5
# print(tuple(a))

# list------>set
# my_list=[2,"vyshnavi",3.5,5,6,]
# print(set(my_list))

# set------->list
# my_set={2,3.4,"vyshnavi,8"}
# print(list(my_set))

# # dictionary------>tuple
# my_dictionary={"name":"vyshnavi","age":19}
# print(tuple(my_dictionary.items()))

# tuple------>dictionary
# my_tuple=((45,35),(5,6),(7,8),(8,9))
# print(dict(my_tuple))

# my_tuple=(["name","vyshnavi"],["roll:no",63],["age",19])
# print(dict(my_tuple))

# # set-------->ductionary
# my_set={("name","vyshanvi"),("age",19)}
# print(dict(my_set))

# explicit type convertion (manual)
# implicit type convertion (automatic)
# number1=5
# number2=2.5
# result=number1+number2
# print(result)         #manual
# print(int(result))     #automatic

# input-------->
# number1=input()
# number2=input()
# result=number1+number2
# print(result)

# number1=int(input("enter any number:"))
# number2=int(input("enter any number:"))
# result=number1+number2
# print(result)

# name=input("enter your name")
# print("hello",name)

# string concatination (+)-------------->
# number1="5" 
# number2="3"
# print(number1+number2)
# print(number1+" "+number2)
# print("vyshnavi"*15)
# print("-"*25)
# print(number1,"\n",number2)
# print(number1,number2,end=" ")

# none------>
# number=None
# print(number)
# print(type(number))

# task 14
# create a float to integer and print the result
# number1=3.5
# print(int(number1))

# task 15
# create a dictionary with 3 key-value pairs and dispaly the output
# my_dictionary={"name":"vyshanvi","age":19,"city":"perumallapuram"}
# print(my_dictionary)

# task 16
# convert integer to complex and complex to float display the output
# number=5
# print(complex(number))
# number=5+6j
# print(float(number.real),float(number.imag))

# task 17
# convert an integer to a string and display the output
# number=8
# print(type(number))
# c=str(number)
# print(type(c))

# task 18
# convert a list to tuple and list to set and tuple to dictionary and dispaly the output
# list=[1,2.3,"vyshnavi"]
# print(tuple(list))
# print(set(list))

# tuple=((6,3.4),(True,"vyshanvi"))
# print(dict(tuple))

# task 19
# take any two strings by using input and concatinate them?
# str1=input("enter any string")
# str2=input("enter any string")
# result=(str1+str2)
# print(result)

# task 20
# repeat your name 15 times by using string operation and display the output?
# print("vyshnavi"*15)

# task 21
# using input write your name and display
# name=input("enter your name :")
# print(name)

# task 22
# write a program that asks the user for two numbers,converts them to integers, subtract them , and print the result
# number1=int(input("enter the number1 :"))
# number2=int(input("enter the number2 :"))
# print(number1-number2)

# task 23
# create a document on list, tuple, set, dictionary(in google docs or word)

# number=5,6
# print(number)

# number=(5,6),(2,8)
# print(dict(number))

# ----------->operators-------->
# a+b here a,b are operands and + is a operator
# types of operator----------->arithmetic operator------->+(addition),-(subtraction),*(multiplication),/(division),%(modulation),**(exponent),//(floor)
                #  ----------->assignment operator------->=,+=,-=,*=,/=,%=,**=,//=
                #  ----------->comparision (relational) operator--------->==,<,>,<=,>=,!=
                #  ----------->logical operator------->AND,OR,NOT
                #  ----------->identity operator----->is,is not
                #  ----------->membership operatoor-------->in, not in

#------------> arithmetic operator------>
# addition(+)------->
# number1=5
# number2=6
# print(number1+number2)

# number1=int(input("enter number1:"))
# number2=int(input ("enter number2:"))
# print(number1+number2)

#subtraction(-)------->
# number1=int(input("enter number1:"))
# number2=int(input("enter number2:"))
# print(number1-number2)

#multiplication(*)------>
# number1=int(input("enter number1:"))
# number2=int(input("enter number2:"))
# print(number1*number2)

#division(/)--------->
# number1=int(input("enter number1:"))
# number2=int(input("enter number2:"))
# print(number1/number2)

# number1=10
# number2=3
# print(round(number1/number2))        

# number1=10
# number2=3
# print(format(number1/number2,".3f"))     #format is used how many numbers u want after point

#modulation(%)----->
# number1=10
# number2=5
# print(number1%number2)         #reminder is output

# number1=13
# number2=5
# print(number1%number2)           #only int value will be output

#exponent(**)------->
# number1=3
# number2=2
# print(number1**number2)          #the number1 will square of number2

#integer division (or) floor division(//)------>
# number1=16
# number2=7
# print(number1//number2)          #only integer division will print

#---------->assignment operator-------->
# compound assignment------------>example:number+=5----->number=number+5

# number=5
# number+=7           #number=number+7
# print(number)

# number=8
# number-=6             #number=number-6
# print(number)

# number=8
# number*=6             #number=number*6
# print(number)

# number=8
# number/=4             #number=number/4
# print(number)

# number=8
# number%=4             #number=number%4
# print(number)

# number=8
# number//=2              #number=number//2
# print(number)

# number=8
# number**=2             #number=number**2
# print(number)

#------------->comparision (or) relational operator--------->
# redmimobile=100
# samsungmobie=150
# print(redmimobile<samsungmobie)        #boolean output
# print(redmimobile>samsungmobie)
# print(redmimobile<=samsungmobie)
# print(redmimobile>=samsungmobie)
# print(redmimobile==samsungmobie)
# print(redmimobile!=samsungmobie)

#------------>logical operator------------> true--->1,flase---->0
#AND gate(multiplication)---------->user name   0    0   1   1
                                #   password    0    1   0   1
                                #   login       0    0   0   1

#OR gate(addition)----------->powerstation  0    0    1   1
                            # inverter      0    1    0   1
                            # result        0    1    1   1

#NOT gate(compliment)--------->0---->1
                              #1---->0

#logical and
# number1=10
# number2=30
# print(number1>5 and number2<50)

# name="vyshnavi"
# password=1234
# print(name=="tanuja" and password==1234)

#logical or
# number1=10
# number2=30
# print(number1>5 or number2>50)

# power_station="on"
# inveter="on"
# print(power_station=="off" or inveter=="on")

#logical not
# a=True
# print(not(a))

# a=25
# b=15
# print(not(a>b))
# print(not(a<b))

#---------->identity operators---------->
#is------>return true if both variables are same objects
#is not--------->return true if both variables are not same objects

# a=10
# b=10
# print(id(a))
# print(id(b))
# print(a is b)

# a=25
# b=15
# print(a is b)
# print(a is not b)

# list_1=[1,2,3]
# list_2=[1,2,3]
# print(id(list_1))
# print(id(list_2))
# print(list_1 is list_2)
# print(list_1 is not list_2)

# list_1=[1,2,3]
# list_2=list_1
# print(id(list_2))
# print(list_1 is list_2)

# list_1=[1,2,3]
# list_2=list_1
# list_1.append(5)
# print(list_1)
# print(list_2)

# task 24
# write a python program that taskes two numbers as input and performs the following operations:
# addition
# subtraction
# multiplication
# division
# modulus
# exponent
# integer (or) floor division
# a=int(input("enter the number1: "))
# b=int(input("enter the number2: "))
# print(a+b)
# print(a-b)
# print(a*b)
# print(a/b)
# print(a**b)
# print(a//b)

# task 25
# initialize a variable x=10. than use each of the following assignment operators and print the result after each step:
# x+=5
# x-=3
# x*=2
# x/=4
# x%=3
# x**=3
# x//=2
# x=10
# x+=5
# print(x)
# x=10
# x-=3
# print(x)
# x=10
# x*=2
# print(x)
# x=10
# x/=4
# print(x)
# x=10
# x%=3
# print(x)
# x=10
# x**=3
# print(x)
# x=10
# x//=2
# print(x)

# task 26
# take two user inputs a and b. use all comparison operators and print whether each condition is true or false.
# a==b
# a!=b
# a>b
# a<b
# a>=b
# a<=b
# a=int(input("enter the number1: "))
# b=int(input("enter the number2: "))
# print(a==b)
# print(a!=b)
# print(a>b)
# print(a<b)
# print(a>=b)
# print(a<=b)

# task 27
# find the area of triangle in python display the output
# b=int(input("enter the value of base: "))
# h=int(input("enter the value of height: "))
# area=0.5*b*h
# print(f"area of triangle: {area}")

# task 28
# take any two variables and check that two variables refer to the same object or not using identity operator
# a=15
# b=15
# print(a is b)
# print(a is not b)

# task 29
# perform logical operators in python and display the output?
# a=20
# b=30
# c=True
# print(a>3 and b<40)
# print(a<1 and b<100)
# print(a==0 or b==9)
# print(not(c))

#----------------> membership oprators------------->
# in---------->returns true if a value is present in the sequence
# not in------------->returns true if a value is not present in the sequence
# works with ---------->string
                    #   list
                    #   tuple
                    #   sets
                    #   dictionaries(only keys,not values)

# numbers=[25,85,98,23,65]
# print(98 in numbers)
# print(100 in numbers)
# print(85 not in numbers)
# print(100 not in numbers)

# word="vyshnavi"
# print("y" in word)
# print("z" not in word)

# my_dictionary={"name":"vyshnavi","age":19}
# print("name" in my_dictionary)
# print("city" in my_dictionary)
# print(19 in my_dictionary)

# ------------>formating (f-strings)----------------->
# number1=5
# number2=8
# print(f"number1={number1}, number2={number2}, multiplication is:{number1*number2}")

# name="vyshanvi"
# age=19
# print(f"my name is {name} and my age is {age}")

# ----------------->indentation------------>
# block of statements
# --------->conditional statement------->
# if statement----------->
# syntax: if condition:

# age=19
# if age>18:
#     print(f"your age is {age} so you are eligible for voating")
#     print("this is if block")
#     print("we are discussing about if statement")

# if-else statement---------->
# syntax: if condition:
        # else :

# age= 19
# if age>18:
#     print(f"your age is {age} so you are eligible for voating")
#     print("this is if block")
# else:
#     print("you are not eligible for voating")
#     print("this is else block")

# colour=input("enter a colour")
# if colour=="red":            
#     print("you can not move")
# else :
#     print("you can move")

# elif statement--------->
# syntax: if condition:
        # elif condition:
        # elif condition:
        #  ............
        # else:

# colour=input("enter the colour")
# if colour=="red":
#     print("you cannot move")
# elif colour=="yellow":
#     print("ready to move")
# elif colour=="green":
#     print("you can move")
# else:
#     print("invalid colour")

#grading system
# marks=int(input("enter your marks"))
# if marks<=100 and marks>=90:
#     print(f"you have obtained {marks}, you have secured O grade")
# elif marks<90 and marks>=80:
#     print(f"you have obtained {marks}, you have secured A grade")
# elif marks<80 and marks>=70:
#     print(f"you have obtained {marks}, you have secured B grade")
# elif marks<70 and marks>=60:
#     print(f"you have obtained {marks}, you have secured C grade")
# elif marks<60 and marks>=50:
#     print(f"you have obtained {marks}, you have secured D grade")
# elif marks<50 and marks>=35:
#     print(f"you have obtained {marks}, you have secured E grade")
# elif marks>=0 and marks<35:
#     print(f"you have obtained {marks}, you have secured F grade")
# else:
#     print("you have entered invalid marks")

# number=int(input("enter your number"))
# if number>0:
#     print(f"number {number} is positive")
# elif number<0:
#     print(f"number {number} is negative")
# else:
#     print("you have entered zero")

# nested if--------->
# number=int(input("enter the number: "))
# if number>0:\
#     print(f"the number {number} is positive")
# elif number<0:
#     print(f"the number {number} is negetive")
# else:
#     print(f"the number {number} is zero")
# short- hand if else----------->
