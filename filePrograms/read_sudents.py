f=open("C:\\Users\\aseed\\OneDrive\\Desktop\\PythonJune\\filePrograms\\students.txt","r")

students=[]

for stud in f:

    students.append(stud.rstrip("\n"))

print(students)

