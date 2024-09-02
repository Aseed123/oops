#fibonaxxi series or not

#0 1 1 2 3 5 8 13 21


number=int(input("Enter the number : "))


previous=0

current=1

is_fibo=False

next=previous+current

if number in (0,1):

    is_fibo=True
else:

 while(next<=number):

    next=previous+current

    previous=current

    current=next

    if next==number:

        is_fibo=True
        
        break

print(f"{number} is Fibonacci" if is_fibo==True else f"{number} is Not Fibonacci")
