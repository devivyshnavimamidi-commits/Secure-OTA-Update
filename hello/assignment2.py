phone_book={
    "vyshnavi":9458755468,
    "surya":98564237,
}
print(phone_book)
phone_book["tanuja"]=9965324187
print(phone_book)
phone_book["vyshnavi"]=9865324715
print(phone_book)
print(phone_book["surya"])

student={
    "python":["vyshnavi",90]
}
print(student)
student["tanuja"]=85
print(student)
student["tanuja"]=88
print(student)
student_search=input("enter a student name")
if student_search in student.keys():
    print("student is exists")
else:
    print("student is not exits")

dictionary={
    "truth":"fact or reality",
    "tall":"of great height",
    "toy":"object for children to play with",
    "travel":"to go from one place to another",
    "tail":"animal end"
}
print(dictionary)
user=input("enter a word")
if user in dictionary.keys():
    print(dictionary[user])
else:
    print("invalid message word is not found try again")

fruit_name={}
fruit=["apple","banana","apple","orange","banana","apple"]
for i in fruit:
    if i not in fruit_name:
        fruit_name[i]=1
    else:
        fruit_name[i]+=1
print(len(fruit_name))
print(fruit_name)

