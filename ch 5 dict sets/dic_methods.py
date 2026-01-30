marks={
     "gs":99,
     "shivam":93,
     "ankit":44,
     "rahul":22,
     "shubham":44
 }

#gives a list of all keys and values
print(marks.items())

#to get only keys
print(marks.keys())


#to get only values
print(marks.values())

marks.update({"gaurav":82})
marks.update({"gs":101}) #updates the value of key 'gs'
print(marks)

print(marks.get("divika")) #returns None as 'divika' key is not present

#marks["Divika"] #returns an error

print(marks.pop("gs"))
print(marks)

item=marks.popitem()#removes and returns a pair(k,v). follows LIFO
print(item)