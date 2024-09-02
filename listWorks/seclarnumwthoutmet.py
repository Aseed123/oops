#wap to print second largest number without using methods

numbers=[11,4,5,6,2,3,1,9,7,8]

largest_num=0

secondlargest_num =0


for i in numbers:

    if i > secondlargest_num and i > largest_num:

        secondlargest_num = largest_num

        largest_num = i

    elif i > secondlargest_num and i < largest_num:

        secondlargest_num = i

print(f"second largest number is {secondlargest_num}")
    
