#lists are just a set of containers to store values of any data types.

#unlike strings lists are mutable
#a list can be indexed just like string

list1=[1,"Gaurav",4.5,True]
print(list1[0])

list1[0]="Grapes"


#it gives index out of range.
#print(list1[4])

print(list1)

list1.append("kill")
print(list1)

#sort method works on list with numbers
l1=[1,44,33,2,99,32,33,-5]
#this sort function sorts the list in ascending order but returns None
l1.sort()
print(l1)

l1.reverse()
print(l1)

l1.insert(3,1999)
print(l1)

#pop method removes the last element from the list and returns it
l1.pop()
print(l1)

l1.pop(2)
print(l1)