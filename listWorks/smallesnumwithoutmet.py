#wap to prin smallest num without using methods

numbers=[4,2,6,4,1,9]

smallest_num=numbers[0]

for i in numbers:

    if i < smallest_num :

        smallest_num = i
    
print(f"smallest number in the list is {smallest_num}")