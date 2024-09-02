 
# number=[0,4,6,8] given list 
# find the missing positive even number from list

number=[0,4,6,8]

max_num = max(number)

missing_even_number = []

for num in range(2, max_num+1, 2):

    if num not in number:

        missing_even_number.append(num)

print(missing_even_number)