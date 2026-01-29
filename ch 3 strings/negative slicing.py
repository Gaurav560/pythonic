name="gaurav"
name_short=name[0:3]
name_negative_sliced=name[-7:-2]
print(name)
print(name_negative_sliced)

    
print(name[:4])
print(name[2:])#it means length

print(name.endswith("array"))

name_of_brother="sameer sharma"

print(name_of_brother.capitalize())#first letter will be capitalized only of the whole String
print(name_of_brother.upper())
print(name_of_brother.lower()) #lowercase all letters
print(name_of_brother.title())#first letter of each word will be capitalized

statement="Gaurav is a great boy. Gaurav is intelligent."
print(statement.count("Gaurav"))
statement_replaced=statement.replace("Gaurav","SAMEER")
print(statement_replaced)
