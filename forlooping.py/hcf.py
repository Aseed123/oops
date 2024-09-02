#gcd of (12,24)#1,2,3,4,,,,,12


num1=int(input("Enter num1:"))

num2=int(input("Enter num2:"))

gcd=1

for i in range(1,num1+1):
    if num1%i==0 and num2%i==0:
     gcd=i
print(f"gcd of {num1},{num2}={gcd}")





