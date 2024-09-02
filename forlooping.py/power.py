#program to find power

# num=int(input("Enter the number: "))#3

# pattern=0

# for i in range(1,num+1):#

#     pattern=pattern*10+num #0*10+3=3,3*10+3=33,33*10+3=333

#     print(pattern)#3 33 333



    #find total of above

num=int(input("Enter the number: "))#3

pattern=0

total=0

for i in range(1,num+1):

    pattern=pattern*10+num 

    total=total+pattern

print(total)
