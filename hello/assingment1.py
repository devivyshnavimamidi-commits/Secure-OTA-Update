list=["vyshnavi","surya","prakash","anu","radha","tanuja"]
print(list[-1])

list=[1,3,5,7,9,11,13,15,17,19]
print(list[2])

list=["red","pink","orange","green","violet"]
print(list[-2])

list=["mango","orange","dragon fruit","grapes","karbuja"]
print(list[2])

list=[1,2,3,4,5,6,7,8,9,10]
print(list[2:6])

list=["a","e","i","o","u"]
print(list[0:3])

list=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
print(list[0:15:2])

list=["c","c++","java","java script",]
list.append("python")
print(list)

list=["vyshnavi","surya","prakash","anu","radha","tanuja"]
list.extend([1,3,2,4,5,6,7])
print(list)

list_1=[1,3,5,7,9]
list_2=[2,4,6,8,10]
list_1.extend(list_2)
print(list_1)

vowels=["a","e","i","o","u"]
consonent=["b","c","d","f","g","h","j","k","l","m","n","p","q","r","s","t","v","w","x","y","z"]
vowels.extend(consonent)
print(vowels)

list=[1,2,1,2,1,2,1,2,1,2,1,2,1,2]
print(list.count(1))

list=[1,4,5,6,7,8,9,44,546,67,7,89,976,48]
for i in range(len(list)):
    print(f"{i} index number")

list=["jan","feb","march","april","may","june","july","aug","sep","oct","nov","dec"]
print(list.index("march"))

list=["cat","dog","elephant","tiger","lion"]
positive=list.index("tiger")
negetive=list.index("tiger")-len(list)
print(positive)
print(negetive)

