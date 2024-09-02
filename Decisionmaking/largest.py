#find largest of two numbers

num1=int(input("Enter first number:"))
num2=int(input("Enter Second number:"))

if num1>num2:
    print(f"{num1} is greater")
elif num2>num1:
    print(f"{num2} is greater")
elif num1==num2:
    print("Both are equal")