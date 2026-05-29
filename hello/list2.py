list=[1,2,3,4,5]
print(list)
print(list.clear())
print(list)

list=["mango","orange","grape"]
print(list)
list[1]="banana"
print(list)

list=["red","green","blue"]
print(list)
list.insert(1,"yellow")
print(list)

list=[3,5,7,5,9]
for i in list:
    if i==5:
     list.remove(5)
     print(list,end=" ")

list=["lion","monkey","pig","elephant"]
print(list.pop(1))
print(list)
print(list.pop(0))
print(list)

list=["biriyani","paneer","chicken","fish","prawn"]
list.reverse()
print(list)

list=[1,4,6,8,10,2,3,5,7,9]
list.sort()
print(list)
list.sort(reverse=True)
print(list)

list=[['sachin',80],['dhoni',92],['virat',85]]
print(list[1][1])

list=['pen','pencil','eraser']
for i,j in enumerate(list):
   print(i,j)
for i,j in enumerate(list):
   print(i+1,j)

print([i for i in range(20,41) if i%2!=0 ])

print([i**2 for i in range(20,31) if i%2==0])

print([i*2 if i%2==0 else 0 for i in range(10,21)])