#prime  or not

number=int(input("Enter the number :"))

isprime=True

for i in range(2,number):

    if number%i==0:

        isprime=False
    
print(f"{number} is prime" if isprime==True else f"{number} Not prime")