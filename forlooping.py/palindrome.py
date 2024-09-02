#palindrome

number=int(input("Enter the number : "))

org=number

result=0

while(number!=0):

    digit=number%10

    result=result*10+digit

    number=number//10

# if (org==result):  

#     print("Palindrome")

# else:

#     print("Not palindrome")

print("Palindrome" if result==org else "Not palindrome")
