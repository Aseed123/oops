#logic1

number=[11,5,7,1,9,10,4]

number.sort()

smallest_num = number[0]

sec_smallest = number[-1]

for  i in number:

    if i < sec_smallest and i < smallest_num:

        sec_smallest = smallest_num

        smallest_num=i

    elif i<sec_smallest and i > smallest_num:

        sec_smallest=i

print(sec_smallest)


#logic2

# number.sort()
# print(number[1])
