#prgrm to print leap year or not

year=int(input("Enter the year: "))

if (year%100==0 and year%400==0) or (year%100!=0 and year%4==0):

    print(f"{year} is Leapyear")

else:
    
    print(f"{year} is not Leapyear")