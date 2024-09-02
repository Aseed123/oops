#write a pprogram to read student name and 3 marks maek1,mark2,mark3 and print total mark and average mark

stud_name=input("Enter the name:")
mark1=input("Enter mark1:")
mark2=input("Enter mark2:")
mark3=input("Enter mark3:")

total_mark=int(mark1)+int(mark2)+int(mark3)
avg_mark=total_mark/3

print(f"Hello {stud_name}")
print(f"total mark={total_mark}")
print(f"average mark={avg_mark}")
