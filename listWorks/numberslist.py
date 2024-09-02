numbers=[10,11,12,34,43,54,19,78,42]

#print number of objects in numbers

print (len(numbers))

#print even numbers in this numbers

for i in range(0,len(numbers)):

    if numbers[i] %2==0:

        print(numbers[i])

#print total of numbers 

total=0

for i in range(0,len(numbers)):

    total=total+numbers[i]

print(total)

#print total of odd numbers in this numbers

total_odd=0

for i in range(0,len(numbers)):
    
    if numbers[i] %2!=0:

        total_odd=total_odd+numbers[i]

print(total_odd)