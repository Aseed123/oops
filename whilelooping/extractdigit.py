#read number and extract digits from number

num=int(input("Enetr the number :"))

while(num!=0):

    digit=num%10

    num=num//10

    print(digit) 