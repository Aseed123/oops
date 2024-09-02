#read a number print sum of digit of cube

num=int(input("Enetr the number : "))

sum=0

while(num%10!=0):

    digit=num%10

    exponent=(digit**3)

    sum=sum+exponent

    num=num//10

print(sum)
