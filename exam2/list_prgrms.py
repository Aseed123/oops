numbers=[10,10,20,20,20,21,22,23]

print(len(numbers))

# Print count of each number

count_num = {}

for num in numbers:
    if num in count_num:
        count_num[num] += 1
    else:
        count_num[num] = 1
print("Count of each number:")
for num, count in count_num.items():
    print(f"{num}: {count}")


#print non repeating numbers

print("Non-repeating numbers:")
for num, count in count_num.items():
    if count == 1:
     print(num)