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
print(marks)