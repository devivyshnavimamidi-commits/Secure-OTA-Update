tuple=("vyshnavi",13,12.5,[1,2,3],(1,4,5))
print(tuple)

tuple=("vyshnavi",13,12.5,[1,2,3],(1,4,5))
print(tuple[1:4:2])

tuple=("vyshnavi",13,12.5,[1,2,3],(1,4,5))
print(tuple[-1])

tuple=("vyshnavi",13,12.5,[1,2,3],(1,4,5))
print(len(tuple))

tuple=("vyshnavi",13,12.5,[1,2,3],(1,4,5))
print(tuple[0:3])

tuple=("vyshnavi",13,12.5,[1,2,3],(1,4,5))
print("vyshnavi" in tuple)
print("tanuja" not in tuple)


in_list=["vyshnavi",8,9,5,4]
a=tuple(in_list)
print(a)

tuple1=(1,2,3,4)
tuple2=(5,6,7,8,)
result=tuple1+tuple2
print(result)

tuple=("vyshnavi",13,12.5,[1,2,3],(1,4,5))
print(tuple*3)

tuple=("vyshnavi",13,12.5,[1,2,3],(1,4,5))
count=tuple.count(13)
print(count)

list1=["vyshnavi","tanuja","surya prakash","anu radha"]
list2=[19,18,48,45]
result=zip(list1,list2)
print(tuple(result))

list1=["vyshnavi","tanuja","surya prakash","anu radha"]
list2=[19,18,48,45]
list3=[90,95,98,91]
result=zip(list1,list2,list3)
print(list(result))

for i in range(6,0,-1):
    for j in range(1,i+1):
        print(i,end=" ")
    print()

for i in range(4,0,-1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()
