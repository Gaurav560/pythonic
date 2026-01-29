#tuple is immutable and ordered collection of items
#tuples are defined using parentheses ()
#tuples can store duplicate values
#tuples can store mixed data types
#tuples support indexing and slicing
#tuples can be nested


#differecnce between list and tuple is that
# list is mutable and tuple is immutable and 
# list is defined using square brackets []
# where as tuple is defined using parentheses ()
# tuples are faster than lists and take less memory & space.

#creating a tuple
#empty tuple
a=()
print(type(a))

#this is not a tuple, it's an integer
b=(1)
print(type(b))

c=(1,)
print(type(c))

tuple_example= (2,"rohan","sameer",4.5,"shivam",True)

#trying to change value in tuple will raise error as tuples are immutable
#tuple_example.append("vrvr")

#a[0]=443 #this will raise error

i=tuple_example.index(4.5)
print(i)