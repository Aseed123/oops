#wap to print largest number without using method 

number=[3,2,5,4,9,1,8,6,7]

largest_num=number[0]

for i in number:

    if i > largest_num:

        largest_num = i

print(f"largest number in the list is {largest_num}")