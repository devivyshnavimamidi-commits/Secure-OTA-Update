set1={1,2,3,1,2,3,1,2,3}
set2={4,5,6,4,5,6,4,5,6}
result=set1.union(set2)
print(result)
result=set1.intersection(set2)
print(result)
result=set1.difference(set2)
print(result)
result=set2.difference(set1)
print(result)
result=set1.symmetric_difference(set2)
print(result)

a={7,8,9,10}
b={7,8,9,10,11,12,13}
result=a.issubset(b)
print(result)
result=b.issuperset(a)
print(result)
result=a.isdisjoint(b)
print(result)

list=[1,2,3,2,3,4,5,3,4,3]
result=set(list)
print(result)
print("-"*23)
set={1, 2, 3, 4, 5}
result=list(set)
print(result)

a=set()
a.add(3)
a.add(4)
a.add(5)
print(a)
a.remove(3)
print(a)
a.discard(3)
print(a)
a.discard(1)
print(a)

fs=[2,3.5,"vyshnavi",(9,10)]
result=frozenset(fs)
print(result)

fs1=frozenset({1,2,7,9})
fs2=frozenset({7,9,6,1})
result=fs1.union(fs2)
print(result)
result=fs1.intersection(fs2)
print(result)
result=fs1.difference(fs2)
print(result)
result=fs2.difference(fs1)
print(result)
result=fs1.issubset(fs2)
print(result)
result=fs2.issubset(fs1)
print(result)
