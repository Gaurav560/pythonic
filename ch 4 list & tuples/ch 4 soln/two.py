mark_of_student_1=int(input("Enter the mark of student 1:"))
mark_of_student_2=int(input("Enter the mark of student 2:"))
mark_of_student_3=int(input("Enter the mark of student 3:"))
mark_of_student_4=int(input("Enter the mark of student 4:"))
mark_of_student_5=int(input("Enter the mark of student 5:"))
mark_of_student_6=int(input("Enter the mark of student 6:"))

marks=[]
marks.append(mark_of_student_1)
marks.append(mark_of_student_2)
marks.append(mark_of_student_3)
marks.append(mark_of_student_4)
marks.append(mark_of_student_5)
marks.append(mark_of_student_6)


#note: sort fn sort in alphabetical order for strings. 
# we have to convert it into int first.
marks.sort()
print(marks)