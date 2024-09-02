#prgrm to print given number is negative,positive or negative

num=int(input("Enter the number:"))

if num>0:
    print(f"{num} is Positive")
elif num==0:
    print(f"{num} is Zero ")
elif num<0:
    print(f"{num} is Negative")
